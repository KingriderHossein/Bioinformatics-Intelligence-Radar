# Contributing

Changes should preserve the separation between evidence authority and editorial framing. Add deterministic behavior to `scripts/` and document interpretation rules in `references/`; do not duplicate a long schema in `SKILL.md`.

Every new event type or state transition should include a fixture and a unit test. Tests must cover both an accepted path and a rejection path, especially for peer-review, preprint identity resolution, duplicate suppression and material updates.

Run the complete local check before opening a change:

```bash
python3 -m unittest discover -s tests -v
python3 -m scripts.radar_cli validate tests/fixtures/items.json
python3 -m scripts.radar_cli run tests/fixtures/items.json --output /tmp/radar-run.json
```

Keep user-visible output in Persian by default, preserve exact English identifiers, and never turn an author-reported benchmark into an independently verified result. Do not commit real credentials, user data, persistent state or generated reports.
