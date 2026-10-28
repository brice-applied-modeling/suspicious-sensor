from src.suspicious_sensor.io.loader import load_data
import pandas as pd
import pytest

def test_load_data_returns_dataframe():
    """Test loading data."""
    result = load_data("pressure_sensor_readings.csv")
    assert isinstance(result, pd.DataFrame)

@pytest.mark.parametrize("filename", [123, None, ["file.csv"], 3.12])
def test_load_data_filename_type(filename):
    """Test that load_data raises TypeError for non-string filename."""
    with pytest.raises(TypeError):
        load_data(filename)

def test_load_data_file_not_found():
    """Test that checks the error handling for a missing data file."""
    with pytest.raises(FileNotFoundError):
        load_data("this_file_should_not_exist.csv")
