import re

import numpy as np
import pandas as pd

# from thefuzz import process


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
        df[col] = df[col].apply(lambda s: re.sub("[a-z]+", " ", str(s)).strip())
        df = df[df[col] != ""]  # drop empt strings
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the data.

    Args:
        df: Preprocessed data.
    Returns:
        Cleaned data, with rows with missing values removed.
    """
    mask = df.amount > 0
    mask |= df.purchase_country == "BR"
    return df[mask].dropna()


def fuzzy_merge(mib: pd.DataFrame, micro_region: pd.DataFrame) -> pd.DataFrame:
    """Merges two dataframes using a fuzzy matching approach.

    Args:
        mib: The left dataframe.
        micro_region: The right dataframe.
    Returns:
        Merged dataframe.
    """
    return mib
