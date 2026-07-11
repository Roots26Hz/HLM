# Week 02 — Data Cleaning & Feature Engineering

> Source guide: `guides/23CSE301_ML_Week2_Guide.pdf`
> Solution notebook: [`lab2_CB.SC.U4CSE24664.ipynb`](lab2_CB.SC.U4CSE24664.ipynb) &nbsp;·&nbsp; Status tracked in the [root dashboard](../../README.md)

## Concepts covered

- _List the key concepts from this week's guide here, then tag them in `meta.yml`._

## Run this week's notebook

```bash
uv run papermill weeks/week02/lab2_CB.SC.U4CSE24664.ipynb .verify_out/week02.ipynb -k python3
```

## Notes

- Datasets: scikit-learn loaders (no downloads). Any CSVs live under `../../data/`.
- Reuse shared helpers: `from ml_utils import load_wine_df, standardize, train_test_split_df`.
