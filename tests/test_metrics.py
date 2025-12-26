import pandas as pd
from nba_value.metrics import cost_per_win_share, efficiency_index, value_index


def test_cost_per_win_share_basic():
    df = pd.DataFrame({"salary": [100.0, 200.0], "win_shares": [10.0, 20.0]})
    out = cost_per_win_share(df)
    assert out.iloc[0] == 10.0
    assert out.iloc[1] == 10.0

def test_efficiency_index_runs():
    df = pd.DataFrame({"vorp": [2.0], "bpm": [3.0], "win_shares": [4.0], "salary": [1.0]})
    out = efficiency_index(df)
    assert out.notna().all()

def test_value_index_range():
    df = pd.DataFrame({
        "vorp": [1.0, 2.0],
        "bpm": [1.0, 2.0],
        "win_shares": [1.0, 2.0],
        "salary": [100.0, 200.0],
    })
    out = value_index(df)
    assert out.min() >= 0.0
    assert out.max() <= 100.0
