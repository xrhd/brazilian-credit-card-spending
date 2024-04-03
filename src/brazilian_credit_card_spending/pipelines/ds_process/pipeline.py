"""
This is a boilerplate pipeline 'ds_process'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import get_model_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=get_model_data,
                inputs=["prim_mibolsillo", "params:expense_groups"],
                outputs="model_data",
            )
        ]
    )
