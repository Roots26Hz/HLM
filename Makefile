# ML Lab Logbook — the only commands you need.
#
#   make install           install/refresh the locked environment
#   make new-week N=2 TITLE="Supervised Learning Basics"
#   make verify            execute every notebook headless (reproducibility gate)
#   make index             regenerate README dashboard + concept index + cheatsheet
#   make check             assert the generated index is in sync (used by CI)

.PHONY: install new-week verify index check

install:
	uv sync

new-week:
	@if [ -z "$(N)" ] || [ -z "$(TITLE)" ]; then \
		echo "usage: make new-week N=<week-number> TITLE=\"<week title>\""; exit 1; \
	fi
	uv run python tools/new_week.py --week $(N) --title "$(TITLE)"

verify:
	uv run python tools/verify_notebooks.py

index:
	uv run python tools/build_index.py

check:
	uv run python tools/build_index.py --check
