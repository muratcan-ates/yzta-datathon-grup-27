import pandas as pd
import numpy as np


# ─── Base features (Sezin) ────────────────────────────────────────────────

def add_sleep_efficiency(df: pd.DataFrame) -> pd.DataFrame:
    """REM + deep sleep percentage sum."""
    df = df.copy()
    df["sleep_efficiency"] = df["rem_yuzdesi"] + df["derin_uyku_yuzdesi"]
    return df


def add_sleep_debt(df: pd.DataFrame) -> pd.DataFrame:
    """Sleep debt relative to 480 minutes (8 hours)."""
    df = df.copy()
    df["sleep_debt"] = (df["uykuya_dalma_suresi_dk"] - 480).clip(lower=0)
    return df


def add_caffeine_screen_interaction(df: pd.DataFrame) -> pd.DataFrame:
    """Interaction term: caffeine x screen time before sleep."""
    df = df.copy()
    df["caffeine_screen_interaction"] = (
        df["uyku_oncesi_kafein_mg"] * df["uyku_oncesi_ekran_suresi_dk"]
    )
    return df


def add_bmi_category(df: pd.DataFrame) -> pd.DataFrame:
    """WHO BMI categories as integer codes."""
    df = df.copy()
    bins = [0, 18.5, 25, 30, 100]
    labels = [0, 1, 2, 3]
    df["bmi_category"] = pd.cut(
        df["vucut_kitle_indeksi"], bins=bins, labels=labels, right=False
    ).astype("Int64")
    return df


def add_age_bins(df: pd.DataFrame) -> pd.DataFrame:
    """Age groups: <25, 25-40, 40-60, 60+"""
    df = df.copy()
    bins = [0, 25, 40, 60, 120]
    labels = [0, 1, 2, 3]
    df["age_bin"] = pd.cut(
        df["yas"], bins=bins, labels=labels, right=False
    ).astype("Int64")
    return df


def add_stress_workload(df: pd.DataFrame) -> pd.DataFrame:
    """Interaction term: stress x daily working hours."""
    df = df.copy()
    df["stress_workload"] = df["stres_skoru"] * df["gunluk_calisma_saati"]
    return df


def add_weekend_recovery(df: pd.DataFrame) -> pd.DataFrame:
    """Positive weekend sleep difference (negative clipped to 0)."""
    df = df.copy()
    df["weekend_recovery"] = df["hafta_sonu_uyku_farki_saat"].clip(lower=0)
    return df


def add_all_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all basic features in order."""
    df = add_sleep_efficiency(df)
    df = add_sleep_debt(df)
    df = add_caffeine_screen_interaction(df)
    df = add_bmi_category(df)
    df = add_age_bins(df)
    df = add_stress_workload(df)
    df = add_weekend_recovery(df)
    return df


# ─── V2 features (Buse) ───────────────────────────────────────────────────

def add_numeric_interactions(df: pd.DataFrame) -> pd.DataFrame:
    """Create numeric interaction features (multiplications).

    Requires: sleep_efficiency (from add_sleep_efficiency).
    """
    df = df.copy()
    df["stress_x_caffeine"] = df["stres_skoru"] * df["uyku_oncesi_kafein_mg"]
    df["sleep_quality_x_steps"] = df["sleep_efficiency"] * df["gunluk_adim_sayisi"]
    df["workhours_x_screen_time"] = df["gunluk_calisma_saati"] * df["uyku_oncesi_ekran_suresi_dk"]
    df["heart_rate_x_stress"] = df["dinlenik_nabiz_bpm"] * df["stres_skoru"]
    return df


def add_ratio_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create ratio features between numeric columns."""
    df = df.copy()
    sleep_hours = df["uykuya_dalma_suresi_dk"] / 60.0
    df["caffeine_per_hour_awake"] = df["uyku_oncesi_kafein_mg"] / (24 - sleep_hours + 1e-6)
    df["screen_to_sleep_ratio"] = df["uyku_oncesi_ekran_suresi_dk"] / (df["uykuya_dalma_suresi_dk"] + 1e-6)
    df["active_to_sedentary"] = df["gunluk_adim_sayisi"] / (df["gunluk_calisma_saati"] + 1e-6)
    return df


def add_polynomial_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create polynomial features for age and stress score (degree 2)."""
    df = df.copy()
    df["yas_squared"] = df["yas"] ** 2
    df["stres_skoru_squared"] = df["stres_skoru"] ** 2
    df["yas_x_stres"] = df["yas"] * df["stres_skoru"]
    return df


def add_binned_numeric_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create binned features for continuous variables.

    Requires: sleep_efficiency (from add_sleep_efficiency).
    """
    df = df.copy()
    stress_bins = [0, 3, 6, 8, 11]
    sleep_bins = [0, 30, 60, 80, 100]
    df["stress_bin"] = pd.cut(
        df["stres_skoru"], bins=stress_bins, labels=[0, 1, 2, 3], right=False
    ).astype("Int64")
    df["sleep_efficiency_bin"] = pd.cut(
        df["sleep_efficiency"], bins=sleep_bins, labels=[0, 1, 2, 3], right=False
    ).astype("Int64")
    return df


def add_cyclical_features(df: pd.DataFrame) -> pd.DataFrame:
    """Encode cyclical features (day of week, month).

    Requires: 'gun' and 'ay' columns in df.
    """
    df = df.copy()
    df["dayofweek_sin"] = np.sin(2 * np.pi * df["gun"] / 7)
    df["dayofweek_cos"] = np.cos(2 * np.pi * df["gun"] / 7)
    df["month_sin"] = np.sin(2 * np.pi * df["ay"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["ay"] / 12)
    return df


def add_all_v2_features(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all v2 feature groups in order."""
    df = add_numeric_interactions(df)
    df = add_ratio_features(df)
    df = add_polynomial_features(df)
    df = add_binned_numeric_features(df)
    df = add_cyclical_features(df)
    return df
