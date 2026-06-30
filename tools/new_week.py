#!/usr/bin/env python3
"""Scaffold a new week folder for the ML Lab Logbook.

Creates ``weeks/weekNN/`` (zero-padded folder) containing:
  - a starter notebook named EXACTLY as the guide demands: ``lab<N>_<rollno>.ipynb``
    (not zero-padded, so it stays gradeable),
  - a ``meta.yml`` stub (the single source of truth that drives all automation),
  - a ``README.md`` from the template,
  - an empty ``figures/`` directory.

Usage:
    python tools/new_week.py --week 2 --title "Supervised Learning Basics"
"""

from __future__ import annotations

import argparse
import sys
import tomllib
from pathlib import Path
from string import Template

import nbformat as nbf

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "tools" / "templates"


def load_config() -> dict:
    with (ROOT / "config.toml").open("rb") as fh:
        return tomllib.load(fh)


def render(template_name: str, **values: str) -> str:
    text = (TEMPLATES / template_name).read_text()
    return Template(text).substitute(**values)


def make_starter_notebook(week: int, title: str, guide: str, notebook: str) -> nbf.NotebookNode:
    nb = nbf.v4.new_notebook()
    nb.cells = [
        nbf.v4.new_markdown_cell(
            f"# Week {week} — {title}\n\n"
            f"Solutions for `{guide}`.\n\n"
            "Work through each topic from the guide: read the Concept, run the Example, "
            "then solve the Exercise below it."
        ),
        nbf.v4.new_code_cell(
            "import numpy as np\n"
            "import pandas as pd\n\n"
            "# Shared, reusable helpers (see shared/ml_utils):\n"
            "from ml_utils import (\n"
            "    load_iris_df,\n"
            "    load_wine_df,\n"
            "    standardize,\n"
            "    train_test_split_df,\n"
            ")\n\n"
            "np.random.seed(42)  # reproducibility"
        ),
        nbf.v4.new_markdown_cell("## Your solutions start here"),
        nbf.v4.new_code_cell("# ..."),
    ]
    nb.metadata.kernelspec = {
        "name": "python3",
        "display_name": "Python 3",
        "language": "python",
    }
    nb.metadata.language_info = {"name": "python"}
    return nb


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a new logbook week.")
    parser.add_argument("--week", type=int, required=True, help="week number, e.g. 2")
    parser.add_argument("--title", required=True, help='week title, e.g. "Supervised Learning"')
    parser.add_argument("--force", action="store_true", help="overwrite existing files")
    args = parser.parse_args()

    if args.week < 1:
        parser.error("--week must be >= 1")

    cfg = load_config()
    rollno = cfg["student"]["rollno"]
    course_code = cfg["course"]["code"]

    padded = f"{args.week:02d}"
    notebook = f"lab{args.week}_{rollno}.ipynb"  # grade-locked name, NOT padded
    guide = f"{course_code}_ML_Week{args.week}_Guide.pdf"

    week_dir = ROOT / "weeks" / f"week{padded}"
    (week_dir / "figures").mkdir(parents=True, exist_ok=True)

    targets = {
        "meta.yml": render(
            "meta.yml.tmpl",
            week=str(args.week),
            title=args.title,
            guide=guide,
            notebook=notebook,
        ),
        "README.md": render(
            "week_readme.md.tmpl",
            week_padded=padded,
            title=args.title,
            guide=guide,
            notebook=notebook,
        ),
    }

    for name, content in targets.items():
        path = week_dir / name
        if path.exists() and not args.force:
            print(f"skip  {path.relative_to(ROOT)} (exists; use --force to overwrite)")
        else:
            path.write_text(content)
            print(f"write {path.relative_to(ROOT)}")

    nb_path = week_dir / notebook
    if nb_path.exists() and not args.force:
        print(f"skip  {nb_path.relative_to(ROOT)} (exists; use --force to overwrite)")
    else:
        nbf.write(make_starter_notebook(args.week, args.title, guide, notebook), nb_path)
        print(f"write {nb_path.relative_to(ROOT)}")

    print(
        f"\nWeek {args.week} scaffolded at weeks/week{padded}/.\n"
        f"Next: solve {notebook}, fill in meta.yml topics, then `make verify` and `make index`."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
