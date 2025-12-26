import numpy as np
import pandas as pd

def cost_per_win_share(df: pd.DataFrame) -> pd.Series:
    ws = df["win_shares"].replace(0, np.nan)
    return df["salary"] / ws

def efficiency_index(df: pd.DataFrame) -> pd.Series:
    """
    Blended impact metric.
    Weights are subjective but explainable.
    """
    return (
        0.6 * df["vorp"] +
        0.3 * df["bpm"] +
        0.1 * df["win_shares"]
    )

def value_index(df: pd.DataFrame) -> pd.Series:
    """
    Impact per dollar, normalized to 0–100.
    Handles edge case where all values are equal (avoids divide-by-zero).
    """
    impact = efficiency_index(df)
    per_dollar = impact / df["salary"]

    mn = per_dollar.min()
    mx = per_dollar.max()

    if pd.isna(mn) or pd.isna(mx) or mx == mn:
        # if we can't scale, just return 0s (or 50s—0 is fine and deterministic)
        return pd.Series([0.0] * len(df), index=df.index)

    return 100 * (per_dollar - mn) / (mx - mn)

def add_kpis(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["cost_per_win_share"] = cost_per_win_share(out)
    out["efficiency_index"] = efficiency_index(out)
    out["value_index"] = value_index(out)
    return out
