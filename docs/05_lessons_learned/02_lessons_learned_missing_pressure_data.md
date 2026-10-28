# Lessons Learned: Handling Missing Pressure Sensor Data

## Context

The Suspicious Sensor dataset contains 4,340 telemetry records. Of these, 75 records have missing `pressure_psi` values.

| Metric | Value |
|---|---:|
| Total records | 4,340 |
| Missing pressure readings | 75 |
| Nonmissing pressure readings | 4,265 |
| Missing percentage | 1.73% |
| Pressure data completeness | 98.27% |

## Key Lesson

**A low percentage of missing values does not, by itself, justify deleting records.** The cause and pattern of missingness matter, particularly in infrastructure telemetry where missing readings may be associated with sensor outages or unusual operating conditions.

## Questions to Investigate Before Cleaning

1. Do missing pressure readings correspond to particular `sensor_status` values, such as `OFFLINE`?
2. Are missing readings scattered across the monitoring period or clustered in time?
3. Are missing readings associated with particular `pump_status` values?
4. Could excluding these periods distort conclusions about pressure behavior or operational risk?

These questions remain to be answered through analysis; the missing-value count alone does not establish the cause.

## Recommended Treatment by Analysis

| Analysis | Treatment |
|---|---|
| Dataset diagnostics | Retain all 4,340 records and report missingness. |
| Pressure mean, variance, and standard deviation | Calculate using nonmissing pressure observations, subject to other validation and duplicate checks. |
| Pressure distribution plots | Use nonmissing pressure values and state the sample size. |
| Sensor reliability and missingness analysis | Retain missing records, timestamps, and operational statuses. |
| Time-series visualization | Preserve timestamps and display gaps rather than silently closing them. |
| Monte Carlo and probability comparisons | Clearly document the sample selection and exclusions. |

## Important Pandas Distinction

Excluding missing values from a **calculation** is not the same as deleting entire rows from the dataset. For example, `df["pressure_psi"].mean()` ignores `NaN` values by default, while the original DataFrame can still retain the timestamps and operating context for those records.

## Preliminary Decision

For the initial descriptive statistics, use the **4,265 nonmissing pressure observations as a starting point**, while retaining the full raw dataset for diagnostic and reliability work. Before finalizing the statistical sample, inspect duplicate timestamps, sensor status, pump status, and other data-quality issues.

This is a **provisional approach**, not evidence that missingness is random or harmless.

## Engineering Implication

A missing pressure reading is **not** evidence of normal pressure. If data gaps coincide with sensor outages or abnormal operating conditions, simply dropping them could underestimate the frequency or severity of pressure excursions.

## Documentation Practice

Record the number and percentage of missing values, the investigation performed, the treatment chosen for each analysis, and any limitations introduced by excluding observations.

**Takeaway:** Diagnose missingness first; then decide which observations belong in each analysis. Preserve the original telemetry and its operational context.
