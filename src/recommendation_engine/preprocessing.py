
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "Dataset.csv"
PROCESSED_DATA_PATH = (
    PROJECT_ROOT / "data" / "processed" / "netflix_cleaned.csv"
)


def clean_data(df):

    df = df.copy()

    # Remove unnecessary spaces from text columns
    text_columns = df.select_dtypes(
        include=["object"]
    ).columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    # Convert placeholder values into missing values
    df.replace(
        ["Not Given", "not given", ""],
        pd.NA,
        inplace=True
    )

    # Fill missing text values
    for column in text_columns:
        if column != "date_added":
            df[column] = df[column].fillna("Unknown")

    # Convert date_added into datetime
    df["date_added"] = pd.to_datetime(
        df["date_added"],
        errors="coerce"
    )

    # Ensure release_year is numeric
    df["release_year"] = pd.to_numeric(
        df["release_year"],
        errors="coerce"
    )

    return df


def main():

    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {RAW_DATA_PATH}"
        )

    df = pd.read_csv(RAW_DATA_PATH)

    cleaned_df = clean_data(df)

    PROCESSED_DATA_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    cleaned_df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

    print("Data cleaning completed successfully!")
    print("Original shape:", df.shape)
    print("Cleaned shape:", cleaned_df.shape)
    print("Saved at:", PROCESSED_DATA_PATH)

    print("\nRemaining missing values:")
    print(cleaned_df.isnull().sum())


if __name__ == "__main__":
    main()

