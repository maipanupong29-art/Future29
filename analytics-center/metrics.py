from __future__ import annotations

import pandas as pd


def rate(series: pd.Series) -> float:
    """Return a 0–100 percentage from a binary/numeric series."""
    if len(series) == 0:
        return 0.0
    return float(series.mean() * 100)
