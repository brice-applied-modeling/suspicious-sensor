"""
Utilities for investigating missing pressure readings before cleaning.

The functions in this module are intended to diagnose whether missing pressure
values appear random or whether they are associated with sensor status, pump
status, or time-based clustering. This helps determine whether excluding missing
records could bias pressure statistics or operational-risk conclusions.
"""

import pandas as pd


def missing_data_investigation(
    df: pd.DataFrame,
    pressure_col: str = "pressure_psi",
    timestamp_col: str = "timestamp",
    sensor_status_col: str = "sensor_status",
    pump_status_col: str = "pump_status",
) -> dict:
    """
    Investigate missing pressure readings before applying cleaning decisions.

    This function is designed to answer the following questions:

    1. What is the count and percentage of missing values for each column?
    2. Do missing pressure readings correspond to particular sensor states,
       such as `OFFLINE`?
    3. Are missing pressure readings scattered across the monitoring period or
       clustered in time?
    4. Are missing pressure readings associated with particular pump states?
    5. Could excluding missing-pressure periods distort conclusions about
       pressure behavior or operational risk?

    Parameters
    ----------
    df : pd.DataFrame
        Input telemetry DataFrame.
    pressure_col : str, default="pressure_psi"
        Name of the pressure-reading column to evaluate for missingness.
    timestamp_col : str, default="timestamp"
        Name of the timestamp column used to evaluate temporal clustering.
    sensor_status_col : str, default="sensor_status"
        Name of the sensor-status column used to compare missing and nonmissing
        pressure records.
    pump_status_col : str, default="pump_status"
        Name of the pump-status column used to compare missing and nonmissing
        pressure records.

    Returns
    -------
    dict
        Dictionary containing:

        - ``missing_summary``:
          DataFrame with missing count and missing percentage for each column.
        - ``missing_pressure_count``:
          Number of records with missing pressure readings.
        - ``missing_pressure_percentage``:
          Percentage of records with missing pressure readings.
        - ``missing_pressure_by_sensor_status``:
          Count and percentage of missing pressure records by sensor status.
        - ``pressure_missing_rate_by_sensor_status``:
          Pressure-missing rate within each sensor-status group.
        - ``missing_pressure_by_pump_status``:
          Count and percentage of missing pressure records by pump status.
        - ``pressure_missing_rate_by_pump_status``:
          Pressure-missing rate within each pump-status group.
        - ``missing_pressure_time_summary``:
          Timestamp range, number of affected dates, and largest gap between
          missing pressure readings.
        - ``missing_pressure_by_date``:
          Daily count of missing pressure readings.
        - ``missing_pressure_rows``:
          Records where pressure is missing, retained for further review.
        - ``risk_note``:
          Plain-language interpretation describing whether dropping missing
          pressure rows could distort conclusions.

    Raises
    ------
    TypeError
        If ``df`` is not a pandas DataFrame.
    ValueError
        If required columns are missing from ``df``.

    Notes
    -----
    This function does not clean or drop records. It preserves missing-pressure
    rows so their timestamp, sensor status, and pump status context can be
    inspected before deciding how each downstream analysis should treat them.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            f"Expected pandas DataFrame, got {type(df).__name__}."
        )

    required_columns = [
        pressure_col,
        timestamp_col,
        sensor_status_col,
        pump_status_col,
    ]
    missing_required_columns = [
        column for column in required_columns if column not in df.columns
    ]

    if missing_required_columns:
        raise ValueError(
            "Missing required columns: "
            f"{', '.join(missing_required_columns)}"
        )

    total_records = len(df)

    missing_counts = df.isna().sum()
    missing_percentages = missing_counts.div(total_records).mul(100)

    missing_summary = (
        pd.DataFrame(
            {
                "missing_count": missing_counts,
                "missing_percentage": missing_percentages,
            }
        )
        .query("missing_count > 0")
        .sort_values(by="missing_percentage", ascending=False)
    )

    pressure_missing_mask = df[pressure_col].isna()
    missing_pressure_rows = df.loc[pressure_missing_mask].copy()
    missing_pressure_count = int(pressure_missing_mask.sum())
    missing_pressure_percentage = (
        missing_pressure_count / total_records * 100
        if total_records > 0
        else 0.0
    )

    missing_pressure_by_sensor_status = _missing_group_summary(
        missing_pressure_rows,
        sensor_status_col,
        missing_pressure_count,
    )
    pressure_missing_rate_by_sensor_status = _missing_rate_by_group(
        df,
        pressure_missing_mask,
        sensor_status_col,
    )

    missing_pressure_by_pump_status = _missing_group_summary(
        missing_pressure_rows,
        pump_status_col,
        missing_pressure_count,
    )
    pressure_missing_rate_by_pump_status = _missing_rate_by_group(
        df,
        pressure_missing_mask,
        pump_status_col,
    )

    missing_pressure_time_summary, missing_pressure_by_date = (
        _missing_time_summary(
            missing_pressure_rows,
            timestamp_col,
        )
    )

    risk_note = _build_risk_note(
        missing_pressure_count=missing_pressure_count,
        missing_pressure_percentage=missing_pressure_percentage,
        missing_pressure_by_sensor_status=missing_pressure_by_sensor_status,
        missing_pressure_by_pump_status=missing_pressure_by_pump_status,
        missing_pressure_time_summary=missing_pressure_time_summary,
    )

    return {
        "missing_summary": missing_summary,
        "missing_pressure_count": missing_pressure_count,
        "missing_pressure_percentage": missing_pressure_percentage,
        "missing_pressure_by_sensor_status": missing_pressure_by_sensor_status,
        "pressure_missing_rate_by_sensor_status": pressure_missing_rate_by_sensor_status,
        "missing_pressure_by_pump_status": missing_pressure_by_pump_status,
        "pressure_missing_rate_by_pump_status": pressure_missing_rate_by_pump_status,
        "missing_pressure_time_summary": missing_pressure_time_summary,
        "missing_pressure_by_date": missing_pressure_by_date,
        "missing_pressure_rows": missing_pressure_rows,
        "risk_note": risk_note,
    }


def _missing_group_summary(
    missing_rows: pd.DataFrame,
    group_col: str,
    missing_count: int,
) -> pd.DataFrame:
    """Summarize missing-pressure records by a categorical grouping column."""
    group_counts = (
        missing_rows[group_col]
        .fillna("UNKNOWN")
        .value_counts(dropna=False)
        .rename("missing_pressure_count")
    )

    group_percentages = (
        group_counts.div(missing_count).mul(100)
        if missing_count > 0
        else group_counts.astype(float)
    )

    return pd.DataFrame(
        {
            "missing_pressure_count": group_counts,
            "missing_pressure_percentage": group_percentages,
        }
    )


def _missing_rate_by_group(
    df: pd.DataFrame,
    missing_mask: pd.Series,
    group_col: str,
) -> pd.DataFrame:
    """Calculate the pressure-missing rate within each categorical group."""
    grouped = (
        pd.DataFrame(
            {
                group_col: df[group_col].fillna("UNKNOWN"),
                "pressure_missing": missing_mask,
            }
        )
        .groupby(group_col)["pressure_missing"]
        .agg(["sum", "count"])
        .rename(
            columns={
                "sum": "missing_pressure_count",
                "count": "total_records",
            }
        )
    )

    grouped["missing_pressure_rate"] = (
        grouped["missing_pressure_count"]
        .div(grouped["total_records"])
        .mul(100)
    )

    return grouped.sort_values(
        by="missing_pressure_rate",
        ascending=False,
    )


def _missing_time_summary(
    missing_rows: pd.DataFrame,
    timestamp_col: str,
) -> tuple[dict, pd.DataFrame]:
    """Summarize when missing-pressure records occur over time."""
    timestamps = pd.to_datetime(
        missing_rows[timestamp_col],
        errors="coerce",
    ).dropna()

    if timestamps.empty:
        return (
            {
                "first_missing_timestamp": pd.NaT,
                "last_missing_timestamp": pd.NaT,
                "affected_dates": 0,
                "largest_gap_between_missing_readings": pd.NaT,
            },
            pd.DataFrame(columns=["missing_pressure_count"]),
        )

    sorted_timestamps = timestamps.sort_values()
    missing_pressure_by_date = (
        sorted_timestamps.dt.date
        .value_counts()
        .sort_index()
        .rename_axis("date")
        .to_frame("missing_pressure_count")
    )

    timestamp_gaps = sorted_timestamps.diff().dropna()
    largest_gap = (
        timestamp_gaps.max()
        if not timestamp_gaps.empty
        else pd.Timedelta(0)
    )

    time_summary = {
        "first_missing_timestamp": sorted_timestamps.min(),
        "last_missing_timestamp": sorted_timestamps.max(),
        "affected_dates": int(sorted_timestamps.dt.date.nunique()),
        "largest_gap_between_missing_readings": largest_gap,
    }

    return time_summary, missing_pressure_by_date


def _build_risk_note(
    missing_pressure_count: int,
    missing_pressure_percentage: float,
    missing_pressure_by_sensor_status: pd.DataFrame,
    missing_pressure_by_pump_status: pd.DataFrame,
    missing_pressure_time_summary: dict,
) -> str:
    """Create a concise interpretation of missing-pressure operational risk."""
    if missing_pressure_count == 0:
        return (
            "No missing pressure readings were found. Excluding missing pressure "
            "records is not expected to affect pressure conclusions because there "
            "are no such records to exclude."
        )

    sensor_statuses_with_missing_pressure = set(
        missing_pressure_by_sensor_status.index.astype(str)
    )

    if sensor_statuses_with_missing_pressure == {"OFFLINE"}:
        return (
            f"All {missing_pressure_count} missing pressure measurements "
            f"({missing_pressure_percentage:.2f}% of records) occurred when "
            "sensor status was OFFLINE. No missing pressure measurements were "
            "observed in NORMAL, DRIFT, or FROZEN states. Missingness is "
            "therefore fully associated with recorded sensor outages. These "
            "observations should be excluded from pressure-based statistics but "
            "retained for sensor reliability and operational data-quality "
            "analysis. The underlying pressure conditions during outages remain "
            "unknown."
        )

    sensor_context = (
        missing_pressure_by_sensor_status.index[0]
        if not missing_pressure_by_sensor_status.empty
        else "UNKNOWN"
    )
    pump_context = (
        missing_pressure_by_pump_status.index[0]
        if not missing_pressure_by_pump_status.empty
        else "UNKNOWN"
    )

    affected_dates = missing_pressure_time_summary.get("affected_dates", 0)

    return (
        f"{missing_pressure_count} pressure readings are missing "
        f"({missing_pressure_percentage:.2f}% of records). The most common "
        f"sensor status among missing pressure records is {sensor_context}, and "
        f"the most common pump status is {pump_context}. Missing readings occur "
        f"across {affected_dates} date(s). Before dropping these rows, inspect "
        "whether the missing records align with sensor outages, pump states, or "
        "time clusters. If they do, excluding them could understate pressure "
        "excursions or operational risk."
    )

def summarize_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize missing data in the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to summarize.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the count and percentage of missing values for each column.
    """
    total_records = len(df)
    missing_counts = df.isna().sum()
    missing_percentages = (missing_counts / total_records) * 100

    summary_df = pd.DataFrame({
        'missing_count': missing_counts,
        'missing_percentage': missing_percentages
    }).sort_values(by='missing_percentage', ascending=False)

    return summary_df

def duplicate_rows_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize duplicate rows in the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to summarize.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the count of duplicate rows and their percentage.
    """
    total_records = len(df)
    duplicate_mask = df.duplicated(keep=False)
    duplicate_count = duplicate_mask.sum()
    duplicate_percentage = (duplicate_count / total_records) * 100

    summary_df = pd.DataFrame({
        'duplicate_count': [duplicate_count],
        'duplicate_percentage': [duplicate_percentage]
    })

    return summary_df

def duplicate_rows_details(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get details of duplicate rows in the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to analyze.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the duplicate rows.
    """
    duplicate_mask = df.duplicated(keep=False)
    duplicate_rows = df[duplicate_mask].copy()

    return duplicate_rows

def get_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get all duplicate rows in the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to analyze.

    Returns
    -------
    pd.DataFrame
        DataFrame containing all duplicate rows.
    """
    duplicate_rows = df[df.duplicated(keep=False)].copy()

    return duplicate_rows

def drop_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop duplicate rows from the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to clean.

    Returns
    -------
    pd.DataFrame
        DataFrame with duplicate rows removed.
    """
    cleaned_df = df.drop_duplicates(keep='first').reset_index(drop=True)

    return cleaned_df

