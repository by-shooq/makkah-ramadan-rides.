"""
Feature engineering pipeline
============================
Turns the public Uber/Lyft (Boston) rides dataset into a simulated
"Makkah during Ramadan" dataset.

NOTE: ramadan_day, prayer_period and the weather columns are SIMULATED
(random, seeded). Results built on top of them demonstrate the pipeline,
not real Makkah behaviour.

Usage:
    python src/feature_engineering.py
    python src/feature_engineering.py --rides data/cab_rides.csv \
        --weather data/weather.csv --out data/Makkah_Ramadan_Rides_Clean.csv
"""

import argparse

import numpy as np
import pandas as pd

SEED = 42

# Boston location -> Makkah landmark
MAKKAH_MAP = {
    "Haymarket Square": "Al-Haram Area",
    "Back Bay": "Aziziyah",
    "North Station": "Haramain Station",
    "South Station": "Kudai Parking",
    "Financial District": "Jabal Omar",
    "Theatre District": "Ajyad",
    "Boston University": "Umm Al-Qura University",
    "Fenway": "Al-Shisha",
    "Beacon Hill": "Al-Misfalah",
}

# Approximate distance (km) from the Haram; anything else falls back to 7.0
DIST_TO_HARAM = {
    "Al-Haram Area": 0.5,
    "Jabal Omar": 0.8,
    "Kudai Parking": 3.5,
    "Aziziyah": 5.2,
}
DEFAULT_DIST_KM = 7.0

PRAYER_PERIODS = ["Fajr", "Iftar", "Tarawih", "Qiyam", "Normal"]
PRAYER_PROBS = [0.1, 0.2, 0.3, 0.2, 0.2]


def load_data(rides_path: str, weather_path: str):
    rides = pd.read_csv(rides_path)  # the file already has a header row
    weather = pd.read_csv(weather_path)

    # Numeric coercion (safe even if the columns are already numeric)
    for col in ("price", "surge_multiplier", "distance"):
        rides[col] = pd.to_numeric(rides[col], errors="coerce")
    print(f"Loaded rides: {len(rides):,} rows | weather: {len(weather):,} rows")
    return rides, weather


def merge_weather(rides: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    """Join rides with the nearest weather reading (same location, <= 1 hour).

    rides.time_stamp is in MILLISECONDS while weather.time_stamp is in SECONDS,
    so a plain merge on 'time_stamp' matches nothing. We convert first and use
    merge_asof to take the closest reading.
    """
    rides = rides.copy()
    rides["ts_sec"] = rides["time_stamp"] // 1000

    weather = weather.rename(columns={"time_stamp": "ts_sec"}).sort_values("ts_sec")
    rides = rides.sort_values("ts_sec")

    merged = pd.merge_asof(
        rides,
        weather,
        on="ts_sec",
        left_by="source",
        right_by="location",
        direction="nearest",
        tolerance=3600,
    )
    print(f"Weather matched for {merged['temp'].notna().mean():.1%} of rides")
    return merged


def localize_to_makkah(df: pd.DataFrame) -> pd.DataFrame:
    df["source"] = df["source"].replace(MAKKAH_MAP)
    df["destination"] = df["destination"].replace(MAKKAH_MAP)
    return df


def add_ramadan_features(df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    n = len(df)
    df["ramadan_day"] = rng.integers(1, 31, size=n)
    df["prayer_period"] = rng.choice(PRAYER_PERIODS, size=n, p=PRAYER_PROBS)
    df["is_last_ten"] = (df["ramadan_day"] > 20).astype(int)
    df["dist_to_haram"] = df["source"].map(DIST_TO_HARAM).fillna(DEFAULT_DIST_KM)
    return df


def simulate_makkah_weather(df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    """Boston weather is not meaningful for Makkah (different units/climate),
    so weather columns are replaced with plausible simulated values."""
    n = len(df)
    df["temp"] = rng.uniform(30, 42, size=n)  # deg C
    df["humidity"] = rng.uniform(20, 60, size=n)  # %
    df["clouds"] = rng.uniform(0, 1, size=n)
    df["rain"] = rng.choice([0, 0.1, 0.5], size=n, p=[0.95, 0.03, 0.02])
    return df


def final_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)
    df = df.dropna(subset=["price"])
    df = df.drop_duplicates()
    # Prices in the source data are USD (2.5 - 97.5); keep a sane range
    df = df[(df["price"] > 2) & (df["price"] < 200)].copy()
    df["ramadan_day"] = df["ramadan_day"].astype(int)
    print(f"Rows: {before:,} -> {len(df):,} after cleaning")
    return df


def main(rides_path: str, weather_path: str, out_path: str) -> pd.DataFrame:
    rng = np.random.default_rng(SEED)

    rides, weather = load_data(rides_path, weather_path)
    df = merge_weather(rides, weather)

    # Drop columns we don't need. Boston weather columns are replaced below.
    df = df.drop(columns=["id", "product_id", "pressure", "wind", "location", "ts_sec"])

    df = localize_to_makkah(df)
    df = add_ramadan_features(df, rng)
    df = simulate_makkah_weather(df, rng)
    df = final_cleaning(df)

    df.to_csv(out_path, index=False)
    print(f"Saved -> {out_path} | shape={df.shape} | nulls={int(df.isnull().sum().sum())}")
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rides", default="data/cab_rides.csv")
    parser.add_argument("--weather", default="data/weather.csv")
    parser.add_argument("--out", default="data/Makkah_Ramadan_Rides_Clean.csv")
    args = parser.parse_args()
    main(args.rides, args.weather, args.out)
