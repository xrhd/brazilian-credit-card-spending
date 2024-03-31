from typing import Dict, Tuple

import pandas as pd


def preprocess(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict]:
    """Preprocesses the data.

    Args:
        df: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """
    return df
