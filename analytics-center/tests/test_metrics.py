import pandas as pd

from app import rate


def test_rate_returns_percentage():
    values = pd.Series([1, 1, 0, 1])
    assert rate(values) == 75.0


def test_rate_handles_empty_series():
    assert rate(pd.Series(dtype=float)) == 0.0
