from src.suspicious_sensor.io.loader import load_data
from src.suspicious_sensor.diagnostics.diagnostics import dataset_diagnostics
import pandas as pd
import pytest



def test_dataset_diagnostics_returns_dictionary():
    """Tests whether dataset diagnostics returns a dictionary."""
    df = load_data("pressure_sensor_readings.csv")
    result = dataset_diagnostics(df)
    assert isinstance(result, dict)

def test_dataset_diagnostics_contains_expected_keys():
    """Tests whether the correct keys are returned."""
    df = load_data("pressure_sensor_readings.csv")
    result = dataset_diagnostics(df)
    expected_keys = {'shape', 'data_types', 'memory_usage', 'unique_values'}
    result_keys_set = set(result.keys())
    assert expected_keys == result_keys_set

def test_dataset_diagnostics_shape_returns_df_shape():
    """Tests that dataset_diagnostics returns the correct DataFrame shape."""
    df = load_data("pressure_sensor_readings.csv")
    result = dataset_diagnostics(df)
    shape = result['shape']
    assert shape == df.shape


def test_dataset_diagnostics_returns_dtypes():
    """Tests whether columns return dtypes."""
    df = load_data("pressure_sensor_readings.csv")
    result = dataset_diagnostics(df)
    actual_dtypes = result['data_types']
    expected_dtypes = df.dtypes
    assert actual_dtypes.equals(expected_dtypes)
    # .dtypes returns a panda Series.
    # Comparing two Series with == produces another Series of booleans,
    # not a single True/False value.
    # Series.equals() returns a single boolean indicating whether
    # the Series has the same values and indices.

def test_dataset_diagnostics_memory_float_greater_than_zero():
    """Tests that the memory was returned as a float and a positive number."""
    df = load_data("pressure_sensor_readings.csv")
    result = dataset_diagnostics(df)
    memory = result['memory_usage']
    assert memory > 0

def test_dataset_diagnostics_reports_unique_values():
    """Tests that unique values are reported."""
    df = load_data("pressure_sensor_readings.csv")
    result = dataset_diagnostics(df)
    actual_unique = result["unique_values"]
    expected_unique = df.nunique().to_dict()
    assert actual_unique == expected_unique

def test_dataset_diagnostics_empty_dataframe():
    """Test that the dataframe contains data."""
    df = load_data("pressure_sensor_readings.csv")
    assert not df.empty

def test_dataset_diagnostics_invalid_input():
    """Test for invalid input."""
    with pytest.raises(TypeError):
        dataset_diagnostics("hello")  # pyright: ignore[reportArgumentType]
