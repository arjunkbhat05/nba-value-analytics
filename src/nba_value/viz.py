import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
from pathlib import Path

from nba_value.etl import build_master, save_master
from nba_value.metrics import add_kpis

PROCESSED_DIR = Path("data/processed")

def build_results() -> pd.DataFrame:
    df = build_master()
    df = add_kpis(df)
    df = df.sort_values("value_index", ascending=False)
    return df

def save_results(df: pd.DataFrame, path: Path = PROCESSED_DIR / "results.csv") -> Path:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path

if __name__ == "__main__":
    results = build_results()
    out_path = save_results(results)
    print(results[["player", "season", "salary", "win_shares", "value_index", "cost_per_win_share"]])
    print("Saved:", out_path)
