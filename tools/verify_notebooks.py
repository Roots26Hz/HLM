#!/usr/bin/env python3
"""Execute every week's notebook headless to prove it reproduces.

This is the reproducibility gate: it runs each ``weeks/*/lab*.ipynb`` from a clean
kernel against the locked environment and exits non-zero if any cell errors. Run
locally via ``make verify`` and automatically in CI on every push.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import papermill as pm

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / ".verify_out"
KERNEL = "python3"


def ensure_kernel() -> None:
    """Register an ipykernel named ``python3`` inside the active environment.

    Uses --sys-prefix so the kernelspec lives in the venv (no global pollution) and
    is discoverable by papermill, which runs from that same environment.
    """
    subprocess.run(
        [
            sys.executable, "-m", "ipykernel", "install",
            "--sys-prefix", "--name", KERNEL, "--display-name", "Python 3 (logbook)",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def find_notebooks() -> list[Path]:
    notebooks = sorted(
        nb
        for nb in ROOT.glob("weeks/*/lab*.ipynb")
        if ".ipynb_checkpoints" not in nb.parts
    )
    return notebooks


def main() -> int:
    notebooks = find_notebooks()
    if not notebooks:
        print("No notebooks found under weeks/*/. Nothing to verify.")
        return 0

    ensure_kernel()
    OUT_DIR.mkdir(exist_ok=True)

    failures: list[tuple[Path, str]] = []
    for nb in notebooks:
        rel = nb.relative_to(ROOT)
        out = OUT_DIR / f"{nb.parent.name}__{nb.name}"
        print(f"running {rel} ...", flush=True)
        try:
            pm.execute_notebook(
                str(nb), str(out), kernel_name=KERNEL, cwd=str(nb.parent), progress_bar=False
            )
            print(f"   OK  {rel}")
        except Exception as exc:  # papermill raises on any cell error
            print(f"  FAIL {rel}")
            failures.append((rel, str(exc).splitlines()[-1] if str(exc) else repr(exc)))

    print()
    if failures:
        print(f"{len(failures)} of {len(notebooks)} notebook(s) failed to reproduce:")
        for rel, msg in failures:
            print(f"  - {rel}: {msg}")
        return 1

    print(f"All {len(notebooks)} notebook(s) reproduced cleanly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
