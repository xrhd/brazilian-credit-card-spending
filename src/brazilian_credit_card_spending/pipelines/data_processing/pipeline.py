"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess,
                inputs="mibolsillo",
                outputs="preprocessed_mibolsillo",
                name="preprocess_node",
            )
        ]
    )
