

import numpy as np
import pandas as pd


def dataset_diagnostics(df: pd.DataFrame) -> dict:
    """
    Ingests DataFrame and performs dataset diagnostics, then returns findings in a dictionary

    Args
    ----
        df (pd.DataFrame):
            DataFrame containing pressure sensor readings.
    Return
    ------
        Results
            Dictionary with the following keys:
                shape - tuple with the shape of the dataset
                data_types - dictionary with column names as keys and data types as values
                memory_usage - how much RAM the dataset consumes
                unique_values - dictionary containing unique value counts for selected columns

    Raises
    ------
    Notes
    -----
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            f"Expected pandas DataFrame, got {type(df).__name__}."
        )

    shape = df.shape
    data_types = df.dtypes
    memory_usage = df.memory_usage(deep=True).sum() / 1024**2
    unique_values = df.nunique().to_dict()
    diagnostic_results = {
        "shape": shape,
        "data_types": data_types,
        "memory_usage": memory_usage,
        "unique_values": unique_values
    }
    return diagnostic_results
