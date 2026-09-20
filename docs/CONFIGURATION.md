# Configuration and Operations

## Quick start

From the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 -m scripts.radar_cli validate tests/fixtures/items.json
python3 -m scripts.radar_cli run tests/fixtures/items.json --state-out /tmp/radar-state.json --output /tmp/radar-run.json
```

The CLI expects a JSON array of discovery items. Search and browser integrations remain outside this repository; their adapters should emit verified primary-source facts before invoking the backend.

Render the processed result into a Persian Markdown report and a downstream-compatible handoff:

```bash
python3 -m scripts.render_output /tmp/radar-run.json \
  --markdown /tmp/radar-report.md \
  --handoff /tmp/telegram-handoff.json
```

## Item minimums

Every item needs `content_type` and a durable identity: DOI/PMID, accession, advisory identifier, repository plus release tag, service event identifier, canonical URL, or primary source URL. Scholarly items additionally require `peer_review_status: verified` and `peer_review_source`. A preprint is never made eligible by a high News Value score.

The six News Value dimensions use integers from 0 to 5: `impact`, `audience_relevance`, `novelty`, `consequence`, `storyability`, and `timeliness`. Evidence quality is handled by gates and provenance, not hidden inside this score.

## Scheduling recommendation

For a daily or twice-daily run, invoke the CLI after an external discovery adapter has refreshed `data/discovered-items.json`, then persist the state atomically and deliver the selected output. For frequent polling, use a durable service with a local queue rather than starting a full AI session for every check. AI newsroom writing should run only after deterministic filtering has reduced the candidate set.

A safe scheduled sequence is:

```text
fetch primary sources → normalize JSON → validate → run with prior state → write new state → render Persian report → deliver
```

Do not enable Telegram or another external delivery adapter until its credentials, target and failure retry policy are configured. Keep `telegram_enabled` false by default.
