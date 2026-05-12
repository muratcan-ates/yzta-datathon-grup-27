import pandas as pd
import numpy as np

def add_numeric_interactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create numeric interaction features (multiplications).

    Generated:
    - stress_x_caffeine
    - sleep_quality_x_steps
    - workhours_x_screen_time
    - heart_rate_x_stress
    """
    df = df.copy()
    df["stress_x_caffeine"] = df["stres_skoru"] * df["uyku_oncesi_kafein_mg"]
    df["sleep_quality_x_steps"] = df["sleep_efficiency"] * df["gunluk_adim_sayisi"]
    df["workhours_x_screen_time"] = df["gunluk_calisma_saati"] * df["uyku_oncesi_ekran_suresi_dk"]
    df["heart_rate_x_stress"] = df["dinlenik_nabiz_bpm"] * df["stres_skoru"]
    return df


def add_ratio_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create ratio features between numeric columns.

    Generated:
    - caffeine_per_hour_awake = uyku_oncesi_kafein_mg / (24 - uyku_suresi)
    - screen_to_sleep_ratio = uyku_oncesi_ekran_suresi_dk / uykuya_dalma_suresi_dk
    - active_to_sedentary = gunluk_adim_sayisi / (gunluk_calisma_saati + 1e-6)
    """
    df = df.copy()
    # uyku süresi = uykuya_dalma_suresi_dk / 60 (saat cinsinden)
    sleep_hours = df["uykuya_dalma_suresi_dk"] / 60.0
    df["caffeine_per_hour_awake"] = df["uyku_oncesi_kafein_mg"] / (24 - sleep_hours + 1e-6)
    df["screen_to_sleep_ratio"] = df["uyku_oncesi_ekran_suresi_dk"] / (df["uykuya_dalma_suresi_dk"] + 1e-6)
    df["active_to_sedentary"] = df["gunluk_adim_sayisi"] / (df["gunluk_calisma_saati"] + 1e-6)
    return df


def add_polynomial_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create polynomial features for age and stress score (degree 2).

    Generated:
    - yas_squared
    - stres_skoru_squared
    - yas_x_stres
    """
    df = df.copy()
    df["yas_squared"] = df["yas"] ** 2
    df["stres_skoru_squared"] = df["stres_skoru"] ** 2
    df["yas_x_stres"] = df["yas"] * df["stres_skoru"]
    return df


def add_binned_numeric_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create binned features for continuous variables.

    Generated:
    - stress_bin (0–3)
    - sleep_efficiency_bin (0–3)
    """
    df = df.copy()
    stress_bins = [0, 3, 6, 8, 11]
    sleep_bins = [0, 30, 60, 80, 100]

    df["stress_bin"] = pd.cut(df["stres_skoru"], bins=stress_bins, labels=[0,1,2,3], right=False).astype("Int64")
    df["sleep_efficiency_bin"] = pd.cut(df["sleep_efficiency"], bins=sleep_bins, labels=[0,1,2,3], right=False).astype("Int64")
    return df


def add_cyclical_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode cyclical features (day of week, month).

    Generated:
    - dayofweek_sin, dayofweek_cos
    - month_sin, month_cos
    """
    df = df.copy()
    # varsayım: df'de 'gun' ve 'ay' kolonları var
    df["dayofweek_sin"] = np.sin(2 * np.pi * df["gun"] / 7)
    df["dayofweek_cos"] = np.cos(2 * np.pi * df["gun"] / 7)
    df["month_sin"] = np.sin(2 * np.pi * df["ay"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["ay"] / 12)
    return df


def add_all_v2_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all v2 feature groups in order.
    """
    df = add_numeric_interactions(df)
    df = add_ratio_features(df)
    df = add_polynomial_features(df)
    df = add_binned_numeric_features(df)
    df = add_cyclical_features(df)
    return df

