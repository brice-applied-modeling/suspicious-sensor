# Dataset Description

## Overview

The Suspicious Sensor dataset is a synthetic infrastructure telemetry dataset designed to simulate realistic operational monitoring conditions commonly encountered in municipal water and wastewater systems.

The dataset represents pressure monitoring data collected from a transmission main feeding a lift station over an extended operational period. While the dataset is synthetic, the anomalies and operating conditions were intentionally designed to resemble issues commonly encountered in real-world telemetry systems.

Unlike many introductory statistics datasets, this dataset intentionally contains operational irregularities, data quality issues, and instrumentation anomalies. The goal is to create a realistic analytical environment where dataset validation and engineering interpretation are just as important as statistical analysis.

The dataset is used throughout this project to explore descriptive statistics, probability theory, Monte Carlo simulation, anomaly detection, and infrastructure analytics.

---

## Dataset File

```text
data/raw/pressure_sensor_readings.csv
```

---

## Dataset Size

| Metric                | Value                              |
| --------------------- | ---------------------------------- |
| Monitoring Period     | Approximately 6 Months             |
| Observation Frequency | Hourly                             |
| Total Records         | ~4,340                             |
| Features              | 6                                  |
| Dataset Type          | Synthetic Infrastructure Telemetry |

---

## Dataset Columns

### timestamp

Timestamp associated with each telemetry observation.

**Data Type:** datetime

Example:

```text
2026-01-01 00:00:00
```

---

### pressure_psi

Observed system pressure measured in pounds per square inch (psi).

This variable represents the primary measurement being investigated throughout the project.

**Data Type:** float

Example:

```text
72.8
```

---

### flow_gpm

Estimated system flow rate measured in gallons per minute (gpm).

Flow values follow realistic daily and weekly operating patterns and are correlated with pressure behavior.

**Data Type:** float

Example:

```text
1652.4
```

---

### sensor_status

Operational status of the telemetry sensor.

Possible values include:

| Status  | Description                                       |
| ------- | ------------------------------------------------- |
| NORMAL  | Sensor operating as expected                      |
| DRIFT   | Sensor gradually deviating from expected behavior |
| FROZEN  | Sensor reporting a repeated value                 |
| OFFLINE | Telemetry unavailable                             |

**Data Type:** string

---

### pump_status

Operational state of the pumping system.

Possible values include:

| Status | Description        |
| ------ | ------------------ |
| ON     | Pump operating     |
| OFF    | Pump not operating |

**Data Type:** string

---

### anomaly_flag

Ground-truth indicator identifying observations that belong to intentionally injected anomalous events.

This field exists primarily for validation and future anomaly detection experiments.

| Value | Description           |
| ----- | --------------------- |
| 0     | Normal Observation    |
| 1     | Anomalous Observation |

**Data Type:** integer

---

## Simulated Operational Behavior

The dataset includes several forms of realistic infrastructure behavior.

### Normal Operating Variation

Pressure and flow fluctuate naturally over time due to changing system demand and operational conditions.

### Daily Demand Cycles

Flow follows a repeating daily pattern intended to mimic customer demand behavior.

### Weekly Demand Patterns

Weekend demand differs from weekday demand to create additional operational variability.

### Pressure-Flow Relationships

Pressure and flow are intentionally correlated to simulate realistic hydraulic system behavior.

---

## Simulated Data Quality Issues

Real infrastructure telemetry systems rarely produce perfect datasets.

To better reflect operational reality, the dataset includes several intentionally injected data quality issues.

### Missing Sensor Readings

Telemetry outages result in missing pressure values throughout the dataset.

Possible real-world causes include:

* communications failures,
* SCADA interruptions,
* sensor outages,
* telemetry packet loss.

### Duplicate Timestamps

A small number of duplicate timestamps are included to simulate:

* historian synchronization issues,
* polling overlap,
* replay events,
* logging inconsistencies.

### Sensor Drift

A prolonged drift event is included where sensor measurements gradually deviate from expected values.

This type of degradation is particularly difficult to identify because it develops slowly over time.

### Frozen Sensor Behavior

A period of repeated values is included to simulate:

* sensor lockup,
* telemetry update failures,
* instrumentation malfunction.

---

## Simulated Operational Events

The dataset contains several operational excursions intended to mimic realistic infrastructure events.

### High Pressure Events

Short-duration pressure spikes are included to simulate:

* pump transitions,
* valve operations,
* hydraulic transients,
* operational disturbances.

### Low Pressure Events

Pressure reductions are included to simulate:

* elevated demand,
* operational constraints,
* system disturbances,
* hydraulic performance issues.

---

## Intended Uses

The dataset was created to support:

* descriptive statistics,
* probability analysis,
* z-score analysis,
* data validation workflows,
* anomaly detection,
* Monte Carlo simulation,
* Bayesian inference,
* infrastructure analytics,
* reliability analysis,
* predictive maintenance experimentation.

---

## Important Note

This dataset is synthetic and should not be interpreted as representing any actual utility system.

The objective is not to perfectly reproduce a specific water or wastewater system, but rather to create a realistic analytical environment where engineering judgment, statistical reasoning, and software development intersect.

Because before predictive models can be trusted, engineers must first determine whether the telemetry itself can be trusted.
