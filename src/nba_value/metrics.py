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
    """
    impact = efficiency_index(df)
    per_dollar = impact / df["salary"]

    # normalize
    return 100 * (per_dollar - per_dollar.min()) / (per_dollar.max() - per_dollar.min())

def add_kpis(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["cost_per_win_share"] = cost_per_win_share(out)
    out["efficiency_index"] = efficiency_index(out)
    out["value_index"] = value_index(out)
    return out
