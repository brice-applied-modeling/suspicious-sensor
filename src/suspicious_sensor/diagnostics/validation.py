"""
Dataset validation checks for pressure sensor telemetry.
"""

import pandas as pd


def dataset_validation(df: pd.DataFrame) -> dict:
    """
    Ingests DataFrame and performs dataset validation, then returns findings in a dictionary.

    Args
    ----
        df (pd.DataFrame):
            DataFrame containing pressure sensor readings.

    Return
    ------
        dict
            Dictionary containing validation results for:
                structure
                data_type
                value_range
                timestamp_validation

    Raises
    ------
        TypeError:
            If the input is not a pandas DataFrame.

    Notes
    -----
        This function is a scaffold for dataset validation checks. It returns a
        structured dictionary so static type checkers and downstream notebook
        code have a stable interface while detailed validation logic is added.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            f"Expected pandas DataFrame, got {type(df).__name__}."
        )
    # validation checks scaffold
    structure_checks = {
        "expected_columns": ["timestamp", "sensor_id", "pressure_reading"],
        "missing_columns": [],
        "extra_columns": [],
    }
    for col in structure_checks["expected_columns"]:
        if col not in df.columns:
            structure_checks["missing_columns"].append(col)
    for col in df.columns:
        if col not in structure_checks["expected_columns"]:
            structure_checks["extra_columns"].append(col)

    data_type_checks = {
        "timestamp": df["timestamp"].dtype if "timestamp" in df.columns else None,
        "sensor_id": df["sensor_id"].dtype if "sensor_id" in df.columns else None,
        "pressure_reading": df["pressure_reading"].dtype if "pressure_reading" in df.columns else None,
    }

    value_range_checks = {
        "pressure_reading": {
            "min": df["pressure_reading"].min() if "pressure_reading" in df.columns else None,
            "max": df["pressure_reading"].max() if "pressure_reading" in df.columns else None,
        }
    }

    timestamp_validation_checks = {
        "timestamp_format": pd.to_datetime(df["timestamp"], errors='coerce').notnull().all() if "timestamp" in df.columns else None,
        "timestamp_range": {
            "min": df["timestamp"].min() if "timestamp" in df.columns else None,
            "max": df["timestamp"].max() if "timestamp" in df.columns else None,
        }
    }

    # Compile all validation results into a single dictionary
    validation_results = {
        "structure": structure_checks,
        "data_type": data_type_checks,
        "value_range": value_range_checks,
        "timestamp_validation": timestamp_validation_checks,
    }

    return validation_results
