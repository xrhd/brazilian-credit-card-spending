import numpy as np
import pandas as pd


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data.

    Args:
        df: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """
    df.amount = df.amount.apply(
        lambda amount: amount.replace("$", "").replace(",", "").replace(" -   ", "-1")
    ).astype(float)
    df.purchase_city = np.where(
        df.purchase_city.str.contains(r"[^\w\s]").infer_objects(copy=False),
        np.nan,
        df.purchase_city,
    )
    for col in ["state", "city", "purchase_city"]:
        df[col] = df[col].str.strip().str.upper()
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the data.

    Args:
        df: Preprocessed data.
    Returns:
        Cleaned data, with rows with missing values removed.
    """
    mask = df.amount > 0
    return df[mask].dropna()
