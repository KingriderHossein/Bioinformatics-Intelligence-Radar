.PHONY: test validate smoke render

test:
	python3 -m unittest discover -s tests -v

validate:
	python3 -m scripts.radar_cli validate tests/fixtures/items.json

smoke:
	python3 -m scripts.radar_cli run tests/fixtures/items.json --output /tmp/radar-run.json

render: smoke
	python3 -m scripts.render_output /tmp/radar-run.json --markdown /tmp/radar-report.md --handoff /tmp/telegram-handoff.json
