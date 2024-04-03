"""
This is a boilerplate pipeline 'ds_process'
generated using Kedro 0.19.3
"""


from typing import Dict, List

import numpy as np
import pandas as pd
from thefuzz import fuzz


def _features(df: pd.DataFrame) -> pd.DataFrame:
    model_data = df[
        ["total_credit_card_limit", "current_available_limit", "amount"]
    ]  # take only numerical columns

    model_data["total_minus_current"] = (
        model_data["total_credit_card_limit"] - model_data["current_available_limit"]
    )
    model_data["current_available_limit_ratio"] = (
        model_data["current_available_limit"] / model_data["total_credit_card_limit"]
    )
    model_data["amount_ratio_from_total"] = (
        model_data["amount"] / model_data["total_credit_card_limit"]
    )
    model_data["amount_ratio_from_current"] = (
        model_data["amount"] / model_data["current_available_limit"]
    )

    model_data["is_F"] = np.where(df.gender == "F", 1, 0)
    model_data["is_M"] = np.where(df.gender == "M", 1, 0)

    model_data["is_the_same_city"] = df.apply(
        lambda row: fuzz.ratio(row.city, row.purchase_city) / 100, axis=1
    )
    model_data["is_the_state"] = df.apply(
        lambda row: fuzz.ratio(row.state, row.geobr_purchase_state) / 100, axis=1
    )
    model_data["is_the_state_conf"] = (
        model_data["is_the_state"] * df["geobr_purchase_city_conf"]
    )

    return model_data


def _labels(df: pd.DataFrame, expense_groups: Dict[str, List[str]]) -> pd.DataFrame:
    # Create a function to assign labels based on expense groups
    def assign_label(expense):
        for group, labels in expense_groups.items():
            if expense in labels:
                return group
        return "Other"

    return df["category_expense"].apply(assign_label)


def get_model_data(
    df: pd.DataFrame, expense_groups: Dict[str, List[str]]
) -> pd.DataFrame:
    model_data = _features(df)
    model_data["label"] = _labels(df, expense_groups)
    model_data["category_expense"] = df["category_expense"]
    return model_data
