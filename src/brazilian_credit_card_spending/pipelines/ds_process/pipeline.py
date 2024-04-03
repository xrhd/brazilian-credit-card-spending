"""
This is a boilerplate pipeline 'ds_process'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, get_model_data, split_data, train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=get_model_data,
                inputs=["prim_mibolsillo", "params:expense_groups"],
                outputs="model_data",
            ),
            node(
                func=split_data,
                inputs=["model_data", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="classifier",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["classifier", "X_test", "y_test"],
                name="evaluate_model_node",
                outputs="metrics",
            ),
        ]
    )
