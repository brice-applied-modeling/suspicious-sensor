# Suspicious Sensor Power BI Dashboard Plan

## Overview

The Suspicious Sensor project provides an excellent opportunity to develop practical Power BI skills while remaining closely aligned with infrastructure engineering, statistics, and applied analytics.

Rather than immediately attempting a large-scale infrastructure reliability project, this dashboard can serve as a smaller proof-of-concept that introduces:

* Data visualization
* Dashboard design
* DAX calculations
* KPI development
* Statistical reporting
* Infrastructure risk communication
* Monte Carlo simulation integration

The lessons learned from this project can later be applied to larger initiatives such as water main failure prediction, asset risk modeling, and the Toronto infrastructure analytics project.

---

# Project Goals

Develop an interactive Power BI dashboard that allows users to:

* Monitor system pressure behavior
* Identify operational anomalies
* Visualize statistical distributions
* Evaluate engineering risk thresholds
* Explore simulated pressure outcomes
* Communicate findings to both engineers and decision-makers

---

# Dashboard Architecture

## Page 1 — Operations Overview

### Purpose

Provide a high-level summary of system performance.

### Key Metrics

* Average Pressure (psi)
* Maximum Pressure
* Minimum Pressure
* Number of High Pressure Events
* Number of Low Pressure Events
* Number of Anomalies

### Visualizations

* KPI Cards
* Pressure Gauge
* Daily Pressure Trend
* Summary Statistics Panel

### Questions Answered

* Is the system operating normally?
* Are pressures remaining within expected ranges?
* Are abnormal events occurring?

---

## Page 2 — Pressure Analysis

### Purpose

Explore the statistical behavior of the pressure readings.

### Visualizations

* Time-Series Pressure Plot
* Histogram
* Box Plot
* Distribution Curve

### Metrics

* Mean
* Median
* Variance
* Standard Deviation

### Questions Answered

* Does the data appear normally distributed?
* Are there outliers?
* Is system behavior drifting over time?

---

## Page 3 — Excursion Monitoring

### Purpose

Track readings outside acceptable operating limits.

### Engineering Thresholds

#### High Pressure

```text
Pressure > 80 psi
```

#### Low Pressure

```text
Pressure < 65 psi
```

### Visualizations

* Excursion Counts
* Excursion Timeline
* Percentage Outside Limits
* Duration of Excursions

### Questions Answered

* How frequently do excursions occur?
* Are excursions isolated or clustered?
* Are pressures becoming increasingly unstable?

---

## Page 4 — Sensor Health Dashboard

### Purpose

Evaluate sensor behavior and anomaly indicators.

### Data Sources

* Sensor Status
* Pump Status
* Anomaly Flag

### Visualizations

* Anomaly Count by Day
* Sensor Status Breakdown
* Pump Status Breakdown
* Anomaly Timeline

### Questions Answered

* Are anomalies increasing?
* Do anomalies correlate with pressure spikes?
* Do pump operations influence abnormal behavior?

---

## Page 5 — Engineering Risk Dashboard

### Purpose

Translate operational data into actionable risk information.

### Example Risk Scoring

```text
Pressure > 80 psi      = 2 points
Pressure < 65 psi      = 3 points
Anomaly Flag Present   = 5 points
```

### Risk Categories

```text
0 – 2   = Low Risk
3 – 6   = Medium Risk
7+      = High Risk
```

### Visualizations

* Risk Score Trend
* Risk Distribution
* High-Risk Event Counts
* Risk Heat Map

### Questions Answered

* When is the system at greatest risk?
* What factors contribute most to risk?
* Are operational issues becoming more frequent?

---

# Monte Carlo Simulation Integration

## Purpose

Introduce probabilistic modeling into the dashboard.

This component provides exposure to simulation-based analytics that can later be applied to infrastructure reliability studies.

### Python Workflow

Generate:

```python
100000 simulated pressure readings
```

Using:

```python
numpy.random.normal()
```

### Export Results

Simulation results can be exported to CSV and imported into Power BI.

### Dashboard Visualizations

* Simulated Distribution
* Analytical vs Simulated Probability
* Confidence Intervals
* Exceedance Probability Curves

### Metrics

Estimate:

* Probability Pressure > 80 psi
* Probability Pressure < 65 psi
* Expected Pressure
* Confidence Intervals

---

# Future Enhancements

Potential future additions include:

## Bayesian Analysis

Estimate:

* Posterior Mean
* Posterior Uncertainty
* Credible Intervals

## Time-Series Analytics

* Rolling Mean
* Rolling Standard Deviation
* Trend Detection
* Seasonal Analysis

## Machine Learning

* Anomaly Detection
* Forecasting
* Classification Models
* Predictive Maintenance

## Reliability Analytics

* Failure Probability Estimation
* Risk-Based Asset Ranking
* Infrastructure Health Scoring

---

# Portfolio Value

This project demonstrates skills across several disciplines:

## Engineering

* Water infrastructure operations
* Pressure system monitoring
* Risk interpretation

## Data Analytics

* Dashboard design
* Statistical analysis
* KPI development

## Data Science

* Monte Carlo simulation
* Probability analysis
* Anomaly detection

## Business Intelligence

* Power BI development
* Interactive reporting
* Decision-support visualization

---

# Long-Term Purpose

This dashboard should be viewed as a foundational infrastructure analytics project.

The objective is not simply to learn Power BI.

The objective is to learn how engineering data can be transformed into information that supports operational decisions, risk management, and future predictive analytics initiatives.
