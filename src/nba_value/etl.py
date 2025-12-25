import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

def load_salaries(path: Path = RAW_DIR / "salaries.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    df["player"] = df["player"].astype(str).str.strip()
    df["season"] = df["season"].astype(str).str.strip()
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
    return df

def load_stats(path: Path = RAW_DIR / "player_stats.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    df["player"] = df["player"].astype(str).str.strip()
    df["season"] = df["season"].astype(str).str.strip()
    for col in ["win_shares", "bpm", "vorp", "gp"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

def build_master() -> pd.DataFrame:
    salaries = load_salaries()
    stats = load_stats()

    merged = pd.merge(
        salaries,
        stats,
        on=["player", "season"],
        how="inner"
    )
    return merged

def save_master(df: pd.DataFrame, path: Path = PROCESSED_DIR / "master.csv") -> Path:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path
