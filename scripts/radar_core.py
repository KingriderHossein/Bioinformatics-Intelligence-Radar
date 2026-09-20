"""Deterministic Radar 3.1 primitives: identity, evidence gates, state and scoring."""
from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import re
from typing import Any, Iterable

PROTOCOL_VERSION = "3.1.0"
SCHOLARLY_TYPES = {"paper", "article", "publication", "review"}
MATERIAL_FIELDS = (
    "content_type", "publication_status", "release_tag", "version", "effective_date",
    "api_state", "schema_state", "authentication_state", "benchmark_revision",
    "independent_validation", "code_data_state", "correction_status", "workflow_impact",
    "evidence_boundary", "event_date",
)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _clean(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: _clean(value[k]) for k in sorted(value) if value[k] not in (None, "", [], {})}
    if isinstance(value, list):
        return [_clean(v) for v in value]
    if isinstance(value, str):
        return re.sub(r"\s+", " ", value.strip()).lower()
    return value


def canonical_id(item: dict[str, Any]) -> str:
    """Return a durable identity; never use an editorial title as the sole key."""
    identifiers = item.get("identifiers", {}) or {}
    content_type = item.get("content_type", "event").lower()
    for key in ("doi", "pmid", "accession", "advisory_id", "canonical_url"):
        if identifiers.get(key):
            return f"{content_type}:{str(identifiers[key]).strip().lower()}"
    if content_type in {"software", "release"}:
        repo = identifiers.get("repository") or item.get("repository")
        tag = item.get("release_tag") or item.get("version")
        if repo and tag:
            return f"software:{repo.strip().lower()}@{tag.strip().lower()}"
    service = identifiers.get("service") or item.get("service")
    if service and identifiers.get("event_id"):
        return f"{content_type}:{service.strip().lower()}:{identifiers['event_id']}"
    source = item.get("primary_source") or item.get("source_url")
    if source:
        return f"{content_type}:url:{source.strip().lower().rstrip('/')}"
    raise ValueError("item needs a durable identifier, canonical URL, or primary source")


def event_fingerprint(item: dict[str, Any]) -> str:
    payload = {key: item.get(key) for key in MATERIAL_FIELDS if item.get(key) not in (None, "", [], {})}
    payload["canonical_id"] = canonical_id(item)
    encoded = json.dumps(_clean(payload), ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()[:20]


def peer_review_eligible(item: dict[str, Any]) -> bool:
    if item.get("content_type", "").lower() not in SCHOLARLY_TYPES:
        return True
    status = str(item.get("peer_review_status", "")).lower()
    return status == "verified" and bool(item.get("peer_review_source")) and not item.get("is_preprint_only", False)


def validate_item(item: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(item, dict):
        return ["item must be an object"]
    if not item.get("content_type"):
        errors.append("content_type is required")
    try:
        canonical_id(item)
    except ValueError as exc:
        errors.append(str(exc))
    if item.get("content_type", "").lower() in SCHOLARLY_TYPES and not peer_review_eligible(item):
        errors.append("scholarly item fails the peer-review gate")
    for score_key in ("impact", "audience_relevance", "novelty", "consequence", "storyability", "timeliness"):
        if score_key in item and (not isinstance(item[score_key], int) or not 0 <= item[score_key] <= 5):
            errors.append(f"{score_key} must be an integer from 0 to 5")
    return errors


def deduplicate(items: Iterable[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Deduplicate within a run; return (unique, suppressed records)."""
    unique: dict[str, dict[str, Any]] = {}
    suppressed: list[dict[str, Any]] = []
    for raw in items:
        item = deepcopy(raw)
        key = canonical_id(item)
        item["canonical_id"] = key
        item["event_fingerprint"] = event_fingerprint(item)
        if key not in unique:
            unique[key] = item
            continue
        current = unique[key]
        # Prefer the item with more claim/evidence detail, while retaining provenance.
        if len(json.dumps(item, ensure_ascii=False)) > len(json.dumps(current, ensure_ascii=False)):
            item.setdefault("merged_sources", []).append(current.get("primary_source"))
            unique[key] = item
        else:
            current.setdefault("merged_sources", []).append(item.get("primary_source"))
        suppressed.append({"canonical_id": key, "reason": "within_run_duplicate"})
    return list(unique.values()), suppressed


def news_value(item: dict[str, Any]) -> dict[str, Any]:
    dimensions = {k: int(item.get(k, 0)) for k in ("impact", "audience_relevance", "novelty", "consequence", "storyability", "timeliness")}
    total = sum(dimensions.values())
    reasons = [f"{key}={value}/5" for key, value in dimensions.items()]
    return {"score": total, "max_score": 30, "dimensions": dimensions, "reason": "; ".join(reasons)}


def classify_against_state(item: dict[str, Any], state: dict[str, Any] | None) -> tuple[str, str | None]:
    if not state or not state.get("ledger"):
        return "NEW", None
    previous = state["ledger"].get(item["canonical_id"])
    if not previous:
        return "NEW", None
    old_fp = previous.get("last_event_fingerprint")
    new_fp = item["event_fingerprint"]
    if old_fp == new_fp:
        return "SUPPRESSED_NO_CHANGE", old_fp
    old_status = str(previous.get("status", ""))
    if item.get("correction_status") in {"correction", "expression_of_concern", "retraction"}:
        return "CORRECTION_OR_RETRACTION", old_fp
    if old_status == "PREPRINT" and item.get("peer_review_status") == "verified":
        return "PUBLICATION_TRANSITION", old_fp
    if old_status in {"PRERELEASE", "NIGHTLY"} and item.get("release_channel") == "stable":
        return "RELEASE_TRANSITION", old_fp
    return "UPDATED", old_fp


def update_state(state: dict[str, Any] | None, items: Iterable[dict[str, Any]], reported_ids: set[str] | None = None) -> dict[str, Any]:
    state = deepcopy(state) if state else {"protocol_version": "1", "ledger": {}, "telemetry": {}}
    state.setdefault("ledger", {})
    state.setdefault("telemetry", {})
    reported_ids = reported_ids or set()
    timestamp = now_iso()
    for item in items:
        key = item["canonical_id"]
        previous = state["ledger"].get(key, {})
        action, _ = classify_against_state(item, state)
        entry = {
            "story_key": key,
            "content_type": item.get("content_type"),
            "canonical_id": key,
            "scientific_title": item.get("title"),
            "first_seen": previous.get("first_seen", timestamp),
            "last_seen": timestamp,
            "last_reported": timestamp if key in reported_ids else previous.get("last_reported"),
            "status": action,
            "last_event_fingerprint": item["event_fingerprint"],
            "last_operational_urgency": item.get("operational_urgency"),
            "last_news_value_score": item.get("news_value", {}).get("score"),
            "last_selected_angle_type": item.get("selected_angle_type"),
            "last_primary_source": item.get("primary_source"),
        }
        state["ledger"][key] = entry
    state["updated_at"] = timestamp
    return state


def process(items: list[dict[str, Any]], state: dict[str, Any] | None = None) -> dict[str, Any]:
    telemetry = {"discovered_unique": 0, "identity_resolved": 0, "peer_review_verified": 0,
                 "excluded_ineligible_scholarly": 0, "cross_run_suppressed_no_change": 0,
                 "material_updates_detected": 0, "story_gate_passed": 0, "newsroom_selected": 0}
    eligible: list[dict[str, Any]] = []
    for item in items:
        errors = validate_item(item)
        if any("peer-review gate" in e for e in errors):
            telemetry["excluded_ineligible_scholarly"] += 1
            continue
        if errors:
            continue
        item = deepcopy(item)
        item["canonical_id"] = canonical_id(item)
        item["event_fingerprint"] = event_fingerprint(item)
        if item.get("content_type", "").lower() in SCHOLARLY_TYPES:
            telemetry["peer_review_verified"] += 1
        telemetry["identity_resolved"] += 1
        eligible.append(item)
    unique, suppressed = deduplicate(eligible)
    telemetry["discovered_unique"] = len(unique)
    selected: list[dict[str, Any]] = []
    for item in unique:
        action, _ = classify_against_state(item, state)
        item["cross_run_action"] = action
        if action == "SUPPRESSED_NO_CHANGE":
            telemetry["cross_run_suppressed_no_change"] += 1
            continue
        if action != "NEW":
            telemetry["material_updates_detected"] += 1
        item["news_value"] = news_value(item)
        if item.get("story_gate_pass", True):
            telemetry["story_gate_passed"] += 1
            selected.append(item)
    selected.sort(key=lambda x: x["news_value"]["score"], reverse=True)
    telemetry["newsroom_selected"] = len(selected)
    return {"protocol_version": PROTOCOL_VERSION, "items": selected, "suppressed": suppressed, "telemetry": telemetry}
