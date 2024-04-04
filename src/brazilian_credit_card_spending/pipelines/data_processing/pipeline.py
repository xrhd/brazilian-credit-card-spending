"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import clean, fuzzy_merge, preprocess


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess,
                inputs="mibolsillo",
                outputs="preprocessed_mibolsillo",
                name="preprocess_node",
            ),
            node(
                func=clean,
                inputs="preprocessed_mibolsillo",
                outputs="cleaned_mibolsillo",
                name="clean_mibolsillo",
            ),
            node(
                func=fuzzy_merge,
                inputs=["cleaned_mibolsillo", "micro_region"],
                outputs="prim_mibolsillo",
                name="fuzzy_merge",
            ),
        ]
    )
