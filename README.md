# ML Lab Logbook — 23CSE301 Machine Learning

> A reproducibility-verified logbook of my weekly ML labs. Every notebook is CI-proven
> to run end-to-end from a clean clone — this is a logbook, not a homework dump.

<!-- Replace USER/REPO once pushed to GitHub so the badge goes live. -->
[![verify](https://github.com/USER/REPO/actions/workflows/verify.yml/badge.svg)](https://github.com/USER/REPO/actions/workflows/verify.yml)
![python](https://img.shields.io/badge/python-3.12-blue)

## What this is

One repository that grows by one folder each week of the semester, but stays coherent:

- **Gradeable** — each week's notebook keeps the exact name the guide demands
  (`lab1_<rollno>.ipynb`, `lab2_<rollno>.ipynb`, …).
- **Reproducible** — pinned with `uv.lock`; CI executes every notebook from a clean clone.
- **Self-indexing** — one tiny `meta.yml` per week auto-generates the dashboard, the
  cross-week concept index, and the cumulative cheat sheet below.
- **Additive** — adding week 12 is the same two-minute ritual as adding week 2.

## Quickstart

```bash
git clone <this-repo> && cd <this-repo>
uv sync                       # install the exact locked environment
uv run jupyter lab           # open and work on notebooks
make verify                   # execute every notebook headless (reproducibility gate)
```

<!-- AUTO:START -->

### Progress

`[####################]` **1/1** weeks complete

### Weeks

| Week | Title | Datasets | Topics | Status | Notebook |
|------|-------|----------|--------|--------|----------|
| 01 | NumPy & Pandas Foundations | `load_iris`, `load_wine` | 20 topics | ✅ done | [`lab1_CB.SC.U4CSE24664.ipynb`](weeks/week01/lab1_CB.SC.U4CSE24664.ipynb) |

### Concept index

Every concept, and the week(s) that cover it:

- **aggregation** — [w01](weeks/week01/)
- **boolean-masking** — [w01](weeks/week01/)
- **broadcasting** — [w01](weeks/week01/)
- **correlation** — [w01](weeks/week01/)
- **encoding** — [w01](weeks/week01/)
- **feature-engineering** — [w01](weeks/week01/)
- **groupby** — [w01](weeks/week01/)
- **indexing-slicing** — [w01](weeks/week01/)
- **linear-algebra** — [w01](weeks/week01/)
- **merging-concat** — [w01](weeks/week01/)
- **missing-data** — [w01](weeks/week01/)
- **numpy-arrays** — [w01](weeks/week01/)
- **pandas-dataframe** — [w01](weeks/week01/)
- **pandas-series** — [w01](weeks/week01/)
- **random-seeding** — [w01](weeks/week01/)
- **reshaping** — [w01](weeks/week01/)
- **selecting-filtering** — [w01](weeks/week01/)
- **sorting-searching** — [w01](weeks/week01/)
- **stacking-splitting** — [w01](weeks/week01/)
- **train-test-split** — [w01](weeks/week01/)

<!-- AUTO:END -->

## Repository layout

```
weeks/weekNN/        one folder per week (zero-padded): notebook + meta.yml + README + figures
shared/ml_utils/     reusable helpers imported by every week (DRY engine)
shared/CHEATSHEET.md auto-generated cumulative quick reference
tools/               automation: new_week, build_index, verify_notebooks
guides/              the source lab-guide PDFs, archived as received
data/                room for CSV datasets in later weeks (sklearn needs none today)
config.toml          one-time settings (roll number, course code)
```

## Adding a new week (the Monday ritual)

```bash
# 1. drop the new guide PDF into guides/
# 2. scaffold the week (auto-names the grade-locked notebook from config.toml)
make new-week N=2 TITLE="Supervised Learning Basics"
# 3. solve the exercises in weeks/week02/lab2_<rollno>.ipynb
# 4. fill in topics/datasets/status in weeks/week02/meta.yml
make verify     # 5. confirm it reproduces
make index      # 6. regenerate the dashboard, concept index, and cheatsheet
# 7. commit & push — CI re-verifies and keeps the badge green
```

## Reproducibility

- Environment pinned via `uv.lock` + `.python-version` (Python 3.12).
- All datasets come from scikit-learn loaders (`load_iris`, `load_wine`) — no downloads.
  CSV datasets in later weeks go under `data/` with documented provenance.
- Random seeds are fixed in every notebook; `make verify` (and CI) prove each notebook
  runs cleanly from a fresh kernel.
