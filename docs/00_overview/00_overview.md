# Project Overview

## Summary

The Suspicious Sensor project is a practice exercise built to simulate realistic infrastructure analytics work for a municipal water utility context. The dataset represents hourly telemetry from a pressure sensor on a transmission main feeding a lift station, along with supporting operational fields such as flow, pump state, sensor state, and anomaly labeling.

Unlike a clean classroom dataset, this project intentionally includes realistic data complications, including missing values, duplicate timestamps, and abnormal operating periods. The purpose is to combine statistical analysis with practical data validation and engineering interpretation.

## Objective

The project objective is to evaluate whether observed pressure behavior is still consistent with the original engineering assumption of a normal pressure model, while developing a repeatable workflow for:

- data loading and validation,
- descriptive statistics and z-score analysis,
- probability estimation using analytical and simulation methods,
- uncertainty-aware interpretation of operational risk.

A secondary objective is to prepare the project structure for future extensions such as anomaly detection, Bayesian inference, and reliability-oriented decision support.

## Scope

### MVP Scope

The MVP focuses on establishing a complete baseline analysis workflow:

- load and validate telemetry data,
- perform data quality checks (missing values, duplicates, datatype verification),
- compute descriptive statistics for pressure,
- run z-score and probability analysis against baseline assumptions,
- perform a Monte Carlo comparison for key pressure thresholds,
- provide an engineering interpretation with documented assumptions and limitations.

### Out of Scope for MVP (Future Phases)

The following are planned as expansion work after core analysis is stable:

- Bayesian parameter estimation and posterior visualization,
- MCMC-based inference workflows,
- anomaly detection model development and benchmarking,
- predictive maintenance and reliability scoring,
- advanced time-series regime-shift and change-point analysis,
- production-grade reporting and operational decision support automation.
