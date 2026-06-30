"""Reusable data helpers for the ML Lab Logbook.

Centralizes boilerplate that every week's notebook would otherwise repeat: loading
scikit-learn toy datasets into tidy DataFrames, standardizing feature matrices, and
making reproducible train/test splits. Import these instead of copy-pasting:

    from ml_utils import load_wine_df, standardize, train_test_split_df
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_wine


def load_iris_df(with_target: bool = True) -> pd.DataFrame:
    """Load the Iris dataset as a DataFrame, optionally with a ``target`` column."""
    ds = load_iris()
    df = pd.DataFrame(ds.data, columns=ds.feature_names)
    if with_target:
        df["target"] = ds.target
    return df


def load_wine_df(with_target: bool = True) -> pd.DataFrame:
    """Load the Wine dataset as a DataFrame, optionally with a ``target`` column."""
    ds = load_wine()
    df = pd.DataFrame(ds.data, columns=ds.feature_names)
    if with_target:
        df["target"] = ds.target
    return df


def standardize(X) -> np.ndarray:
    """Standardize features column-wise to zero mean / unit variance.

    Zero-variance columns are left centered (divided by 1) to avoid NaNs.
    """
    X = np.asarray(X, dtype=float)
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    std = np.where(std == 0, 1.0, std)
    return (X - mean) / std


def train_test_split_df(
    df: pd.DataFrame, test_size: float = 0.2, seed: int = 42
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Reproducibly shuffle and split a DataFrame into ``(train, test)``.

    Mirrors the hand-rolled ``.sample(frac=1)`` + ``.iloc`` split taught in the labs,
    but with a fixed seed so results are identical on every run and every machine.
    """
    shuffled = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    n_test = int(round(len(shuffled) * test_size))
    test = shuffled.iloc[:n_test].reset_index(drop=True)
    train = shuffled.iloc[n_test:].reset_index(drop=True)
    return train, test
