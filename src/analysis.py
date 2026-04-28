# Global Meteorite Landings Analysis 2026

# This project explores meteorite landings data using Python, pandas, and matplotlib.
# The analysis answers questions about meteorite frequency, types, mass, timing, and location.

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "meteorite_landings.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"
TABLES_DIR = OUTPUT_DIR / "tables"

FIGURES_DIR.mkdir(parents=True, exist_ok=True)
TABLES_DIR.mkdir(parents=True, exist_ok=True)

def load_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["reclat", "reclong", "year", "mass (g)"])
    df = df[(df["reclat"] != 0) & (df["reclong"] != 0)]
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["mass (g)"] = pd.to_numeric(df["mass (g)"], errors="coerce")
    df = df.dropna(subset=["year", "mass (g)"])
    df = df[(df["year"] >= 1800) & (df["year"] <= 2026)]
    df["year"] = df["year"].astype(int)
    return df

def analyse_fall(df: pd.DataFrame) -> pd.Series:
    return df["fall"].value_counts()        # 1. Fell vs Found

def analyse_recclass(df: pd.DataFrame) -> pd.Series:
    return df["recclass"].value_counts().head(10)

def analyse_largest(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values("mass (g)", ascending=False)[["name", "mass (g)", "year", "recclass"]].head(5)

def analyse_yearly(df: pd.DataFrame) -> pd.Series:
    return df["year"].value_counts().sort_index()

def analyse_locations(df: pd.DataFrame) -> pd.Series:
    return df[["reclat", "reclong"]].value_counts().head(10)

def save_outputs(df: pd.DataFrame) -> None:
    fall = analyse_fall(df)
    recclass = analyse_recclass(df)
    largest = analyse_largest(df)
    yearly = analyse_yearly(df)
    locations = analyse_locations(df)

    fall.to_csv(TABLES_DIR / "fall_vs_found.csv")                   # 1. Fell vs Found
    recclass.to_csv(TABLES_DIR / "top_10_recclass.csv")             # 2. Most common meteorite types
    largest.to_csv(TABLES_DIR / "top_5_largest_meteorites.csv")     # 3. Larget meteorites
    yearly.to_csv(TABLES_DIR / "meteorites_per_year.csv")           # 4. Meteorites recorded over time
    locations.to_csv(TABLES_DIR / "top_10_locations.csv")           # 5. Where meteorites land most often

    plt.figure(figsize=(10, 5))
    yearly.plot()
    plt.xlabel("Year")
    plt.ylabel("Number of meteorites")
    plt.title("Meteorite discoveries per year")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "meteorite_discoveries_per_year.png", dpi=300)
    plt.close()

def main() -> None:
    meteor = load_data(DATA_PATH)
    print(meteor.info())
    print(meteor.describe())
    meteor = clean_data(meteor)

    print("\nFell vs Found:")
    print(analyse_fall(meteor))

    print("\nMost common meteorite types:")
    print(analyse_recclass(meteor))

    print("\nLargest meteorites:")
    print(analyse_largest(meteor))

    print("\nMeteorites recorded over time:")
    yearly = analyse_yearly(meteor)
    print(yearly)

    print("\nMost common locations:")
    print(analyse_locations(meteor))

    save_outputs(meteor)

    print("\nLast 20 years:")
    print(yearly.tail(20))

if __name__ == "__main__":
    main()

# ------------------------------------------------------------------------------------------------------------
# CONCLUSION

# This project explored global meteorite landings using Python and pandas.
# The analysis showed that most records are classified as found rather than fell,
# and that meteorite classes and masses vary widely. Some data quality issues were also identified,
# including missing coordinates and unusual year values, which were handled during cleaning.
# Overall, this project built a strong foundation for exploratory data analysis and future dashboard work.