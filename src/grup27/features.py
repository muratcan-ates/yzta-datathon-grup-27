import pandas as pd
import numpy as np


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
