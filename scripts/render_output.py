"""Render deterministic Radar results into Persian Markdown and Handoff v1."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def render_markdown(result: dict[str, Any], reporting_window: str = "") -> str:
    items = result.get("items", [])
    lead = items[0] if items else None
    follow = items[1:5]
    lines = ["# رادار بیوانفورماتیک — گزارش اجرایی", "", f"`بازه رصد: {reporting_window or 'ثبت نشده'}`", ""]
    if lead:
        lines += ["## ۱. خبر اول", "", f"### {lead.get('title', 'بدون عنوان')}", "", lead.get("news_statement_fa") or lead.get("summary_fa") or "این مورد پس از عبور از دروازه‌های شواهد و خبر انتخاب شده است.", "", f"منبع: {lead.get('primary_source', 'ثبت نشده')}", ""]
    else:
        lines += ["## ۱. خبر اول", "", "امروز خبر اولی که از نظر شواهد و اهمیت از سایر موارد متمایز باشد انتخاب نشد.", ""]
    lines += ["## ۲. ارزش دنبال‌کردن", ""]
    if not follow:
        lines.append("مورد دیگری برای دنبال‌کردن در این اجرای پایش انتخاب نشد.")
    for item in follow:
        lines += [f"### {item.get('title', 'بدون عنوان')}", "", item.get("summary_fa") or item.get("news_statement_fa") or "جزئیات در Evidence Card ثبت شده است.", "", f"امتیاز News Value: {item.get('news_value', {}).get('score', 'ثبت نشده')}/30", f"منبع: {item.get('primary_source', 'ثبت نشده')}", ""]
    lines += ["## ۳. پایش امروز", "", "```json", json.dumps(result.get("telemetry", {}), ensure_ascii=False, indent=2), "```", ""]
    return "\n".join(lines)


def telegram_handoff(result: dict[str, Any]) -> dict[str, Any]:
    candidates = []
    for item in result.get("items", [])[:5]:
        candidates.append({
            "candidate_id": item.get("canonical_id"),
            "evidence_card_id": item.get("canonical_id"),
            "title": item.get("title"),
            "headline_options": item.get("headline_options", []),
            "news_statement_fa": item.get("news_statement_fa"),
            "primary_source": item.get("primary_source"),
            "limitations": item.get("limitations", []),
            "do_not_say_fa": item.get("do_not_say_fa", []),
            "peer_review_verified": item.get("peer_review_status") == "verified" if item.get("content_type") in {"paper", "article", "publication", "review"} else None,
            "news_value_score": item.get("news_value", {}).get("score"),
            "format_recommendation": item.get("format_recommendation", "Telegram"),
        })
    return {"handoff_version": "1.0", "source_protocol": result.get("protocol_version", "3.1.0"), "candidates": candidates}


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Render Radar result JSON")
    parser.add_argument("input")
    parser.add_argument("--markdown")
    parser.add_argument("--handoff")
    args = parser.parse_args()
    result = json.loads(Path(args.input).read_text(encoding="utf-8"))
    if args.markdown:
        Path(args.markdown).write_text(render_markdown(result), encoding="utf-8")
    if args.handoff:
        Path(args.handoff).write_text(json.dumps(telegram_handoff(result), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not args.markdown and not args.handoff:
        print(render_markdown(result))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
