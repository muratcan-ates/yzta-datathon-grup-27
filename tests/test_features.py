import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
from grup27.features import (
    add_numeric_interactions, add_ratio_features,
    add_polynomial_features, add_binned_numeric_features,
    add_cyclical_features, add_all_v2_features
)

def make_df():
    return pd.DataFrame({
        "stres_skoru": [5, 8],
        "uyku_oncesi_kafein_mg": [100, 50],
        "sleep_efficiency": [70, 80],
        "gunluk_adim_sayisi": [5000, 8000],
        "gunluk_calisma_saati": [8, 10],
        "uyku_oncesi_ekran_suresi_dk": [30, 60],
        "dinlenik_nabiz_bpm": [70, 80],
        "yas": [25, 40],
        "uykuya_dalma_suresi_dk": [420, 500],
        "gun": [1, 5],
        "ay": [3, 7],
    })

def test_add_numeric_interactions():
    df = add_numeric_interactions(make_df())
    assert "stress_x_caffeine" in df.columns
    assert df["stress_x_caffeine"].iloc[0] == 500
    assert "sleep_quality_x_steps" in df.columns

def test_add_ratio_features():
    df = add_ratio_features(make_df())
    assert "caffeine_per_hour_awake" in df.columns
    assert "screen_to_sleep_ratio" in df.columns

def test_add_polynomial_features():
    df = add_polynomial_features(make_df())
    assert "yas_squared" in df.columns
    assert df["yas_squared"].iloc[0] == 625

def test_add_binned_numeric_features():
    df = add_binned_numeric_features(make_df())
    assert "stress_bin" in df.columns
    assert "sleep_efficiency_bin" in df.columns

def test_add_cyclical_features():
    df = add_cyclical_features(make_df())
    assert "dayofweek_sin" in df.columns
    assert "month_cos" in df.columns

def test_add_all_v2_features():
    df = add_all_v2_features(make_df())
    for col in [
        "stress_x_caffeine", "caffeine_per_hour_awake",
        "yas_squared", "stress_bin", "dayofweek_sin"
    ]:
        assert col in df.columns
