
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = PROJECT_ROOT / "data" / "raw" / "Dataset.csv"

def load_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    print("\nDataset loaded successfully!")
    print("Shape:", df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    return df


if __name__ == "__main__":
    load_data()


def explore_data(df):

    print("\n========== DATA TYPES ==========")
    print(df.dtypes)

    print("\n========== DUPLICATE RECORDS ==========")
    print("Duplicate rows:", df.duplicated().sum())
    print("Duplicate show_id:", df["show_id"].duplicated().sum())
    print("Duplicate titles:", df["title"].duplicated().sum())

    print("\n========== CONTENT TYPE DISTRIBUTION ==========")
    print(df["type"].value_counts())

    print("\n========== TOP 10 COUNTRIES ==========")
    print(df["country"].value_counts().head(10))

    print("\n========== TOP 10 GENRES ==========")
    genres = (
        df["listed_in"]
        .dropna()
        .str.split(", ")
        .explode()
    )
    print(genres.value_counts().head(10))

    print("\n========== RELEASE YEAR RANGE ==========")
    print("Oldest:", df["release_year"].min())
    print("Newest:", df["release_year"].max())

    print("\n========== UNIQUE VALUES ==========")
    for column in ["type", "rating", "duration"]:
        print(f"\n{column}:")
        print(df[column].value_counts().head(10))


if __name__ == "__main__":
    df = load_data()
    explore_data(df)
