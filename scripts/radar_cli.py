#!/usr/bin/env python3
"""CLI for Radar 3.1 deterministic backend operations."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .radar_core import process, update_state, validate_item


def load_json(path: str):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save_json(path: str, data) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Bioinformatics Intelligence Radar 3.1")
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate", help="validate items against evidence gates")
    validate.add_argument("input")
    run = sub.add_parser("run", help="deduplicate, classify and score a JSON item collection")
    run.add_argument("input")
    run.add_argument("--state")
    run.add_argument("--output", "-o")
    run.add_argument("--state-out")
    args = parser.parse_args()
    payload = load_json(args.input)
    items = payload if isinstance(payload, list) else payload.get("items", [])

    if args.command == "validate":
        checks = [{"index": i, "errors": validate_item(item)} for i, item in enumerate(items)]
        output = {"valid": all(not check["errors"] for check in checks), "items": checks}
    else:
        state = load_json(args.state) if args.state else None
        output = process(items, state)
        if args.state_out:
            updated = update_state(state, output["items"], {x["canonical_id"] for x in output["items"]})
            save_json(args.state_out, updated)

    text = json.dumps(output, ensure_ascii=False, indent=2) + "\n"
    if getattr(args, "output", None):
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0 if output.get("valid", True) else 1


if __name__ == "__main__":
    raise SystemExit(main())
