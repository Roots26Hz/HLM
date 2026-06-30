"""ml_utils — cumulative, reusable helpers shared across every week's lab.

Keep this package DRY: whenever a piece of boilerplate shows up in two notebooks,
promote it here so later weeks import it instead of copy-pasting.
"""

from ml_utils.data import (
    load_iris_df,
    load_wine_df,
    standardize,
    train_test_split_df,
)

__all__ = [
    "load_iris_df",
    "load_wine_df",
    "standardize",
    "train_test_split_df",
]
