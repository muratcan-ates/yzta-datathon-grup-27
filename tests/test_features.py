import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
from grup27.features import (
    # Base features (Sezin)
    add_sleep_efficiency, add_sleep_debt,
    add_caffeine_screen_interaction, add_bmi_category,
    add_age_bins, add_stress_workload,
    add_weekend_recovery, add_all_basic_features,
    # V2 features (Buse)
    add_numeric_interactions, add_ratio_features,
    add_polynomial_features, add_binned_numeric_features,
    add_cyclical_features, add_all_v2_features,
)


def make_df():
    return pd.DataFrame({
        # Sezin base columns
        "rem_yuzdesi": [20.0, 25.0],
        "derin_uyku_yuzdesi": [15.0, 10.0],
        "uykuya_dalma_suresi_dk": [420.0, 500.0],
        "uyku_oncesi_kafein_mg": [100.0, 50.0],
        "uyku_oncesi_ekran_suresi_dk": [30.0, 60.0],
        "vucut_kitle_indeksi": [22.0, 27.0],
        "yas": [25.0, 40.0],
        "stres_skoru": [5.0, 8.0],
        "gunluk_calisma_saati": [8.0, 10.0],
        "hafta_sonu_uyku_farki_saat": [1.5, -0.5],
        # Buse v2 columns
        "sleep_efficiency": [70.0, 80.0],
        "gunluk_adim_sayisi": [5000.0, 8000.0],
        "dinlenik_nabiz_bpm": [70.0, 80.0],
        "gun": [1, 5],
        "ay": [3, 7],
    })


# ─── Base feature tests (Sezin) ───────────────────────────────────────────

def test_sleep_efficiency():
    df = add_sleep_efficiency(make_df())
    assert "sleep_efficiency" in df.columns
    assert df["sleep_efficiency"].iloc[0] == 35.0


def test_sleep_debt():
    df = add_sleep_debt(make_df())
    assert "sleep_debt" in df.columns
    assert df["sleep_debt"].iloc[0] == 0.0
    assert df["sleep_debt"].iloc[1] == 20.0


def test_caffeine_screen_interaction():
    df = add_caffeine_screen_interaction(make_df())
    assert "caffeine_screen_interaction" in df.columns
    assert df["caffeine_screen_interaction"].iloc[0] == 3000.0


def test_bmi_category():
    df = add_bmi_category(make_df())
    assert "bmi_category" in df.columns
    assert df["bmi_category"].iloc[0] == 1
    assert df["bmi_category"].iloc[1] == 2


def test_age_bins():
    df = add_age_bins(make_df())
    assert "age_bin" in df.columns
    assert df["age_bin"].iloc[0] == 1
    assert df["age_bin"].iloc[1] == 2


def test_stress_workload():
    df = add_stress_workload(make_df())
    assert "stress_workload" in df.columns
    assert df["stress_workload"].iloc[0] == 40.0


def test_weekend_recovery():
    df = add_weekend_recovery(make_df())
    assert "weekend_recovery" in df.columns
    assert df["weekend_recovery"].iloc[0] == 1.5
    assert df["weekend_recovery"].iloc[1] == 0.0


def test_add_all_basic_features():
    df = add_all_basic_features(make_df())
    for col in [
        "sleep_efficiency", "sleep_debt", "caffeine_screen_interaction",
        "bmi_category", "age_bin", "stress_workload", "weekend_recovery",
    ]:
        assert col in df.columns


# ─── V2 feature tests (Buse) ──────────────────────────────────────────────

def test_add_numeric_interactions():
    df = add_numeric_interactions(make_df())
    assert "stress_x_caffeine" in df.columns
    assert df["stress_x_caffeine"].iloc[0] == 500.0
    assert "sleep_quality_x_steps" in df.columns


def test_add_ratio_features():
    df = add_ratio_features(make_df())
    assert "caffeine_per_hour_awake" in df.columns
    assert "screen_to_sleep_ratio" in df.columns


def test_add_polynomial_features():
    df = add_polynomial_features(make_df())
    assert "yas_squared" in df.columns
    assert df["yas_squared"].iloc[0] == 625.0


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
        "yas_squared", "stress_bin", "dayofweek_sin",
    ]:
        assert col in df.columns
