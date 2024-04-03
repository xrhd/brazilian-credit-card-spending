"""
This is a boilerplate pipeline 'ds_process'
generated using Kedro 0.19.3
"""

import logging
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
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
    """Prepare data for model training.

    Args:
        df: Data containing features and target.
        expense_groups: Dictionary of expense groups.
    Returns:
        Data for model training.
    """
    model_data = _features(df)
    model_data["label"] = _labels(df, expense_groups)
    model_data["category_expense"] = df["category_expense"]
    return model_data


def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X = data[parameters["features"]]
    y = data[parameters["label"]]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=parameters["test_size"],
        random_state=parameters["random_state"],
        stratify=y,
    )
    return X_train, X_test, y_train, y_test


def train_model(
    X_train: pd.DataFrame, y_train: pd.Series
) -> HistGradientBoostingClassifier:
    """Trains the classifier model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    clf = HistGradientBoostingClassifier().fit(X_train, y_train)
    return clf


def evaluate_model(
    classifier: HistGradientBoostingClassifier, X_test: pd.DataFrame, y_test: pd.Series
) -> Dict[str, float]:
    """Calculates and logs the most popular classification metrics.

    Args:
        classifier: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    logger = logging.getLogger(__name__)
    y_pred = classifier.predict(X_test)

    report_txt = classification_report(y_test, y_pred)
    logger.info(report_txt)
    report = classification_report(y_test, y_pred, output_dict=True)

    metrics = pd.json_normalize(report, sep="_")
    metrics = metrics.to_dict(orient="records")[0]
    logger.info(metrics)
    return metrics
