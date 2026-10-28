# The Suspicious Sensor  
*A Probability, Statistics, and Monte Carlo Exercise*

---

# Scenario

A water utility installs a pressure sensor on a transmission main feeding a lift station.

The engineers believe the pressure fluctuations follow a normal distribution:

```text
μ = 72 psi
σ = 4 psi
```

However, after several months, operators suspect the system may actually be experiencing abnormal pressure instability.

Operational telemetry is collected over an extended monitoring period for analysis.

This exercise uses a realistic synthetic dataset with hourly records and operational artifacts that often appear in real infrastructure systems.

See `data/raw/pressure_sensor_readings.csv` for the dataset.

Your task is to investigate whether the system still appears consistent with the original assumptions.

For the current project snapshot, the dataset contains approximately:

- 6 months of hourly telemetry (Jan 2026 to Jun 2026),
- 4,340 total records,
- 6 columns: `timestamp`, `pressure_psi`, `flow_gpm`, `sensor_status`, `pump_status`, `anomaly_flag`,
- intentional data quality issues (missing pressure values during `OFFLINE`, duplicate timestamps, and status-specific anomalies),
- intentionally injected abnormal operating periods (high/low pressure events, drift, frozen values).

Important: this is not a perfectly clean one-variable classroom dataset. It is intentionally designed to require both statistical analysis and data validation with engineering judgment.

Because infrastructure systems never simply behave quietly and respectfully for decades. That would apparently violate the laws of engineering.

---

# Data Context and Assumptions

Before starting the formal parts below, assume the following:

1. `pressure_psi` is the primary variable for Parts A-E and Bonus.
2. `flow_gpm`, `pump_status`, and `sensor_status` provide operating context.
3. `anomaly_flag` is available as ground truth for validation and comparison, not as a replacement for your own reasoning.
4. You should explicitly decide whether each calculation is performed on:
   - raw data,
   - cleaned data,
   - or both.

Document your preprocessing decisions, especially for:

- missing pressure values,
- duplicate timestamps,
- non-`NORMAL` sensor states,
- obvious telemetry artifacts.

Treat these preprocessing choices as part of the exercise deliverable, not just background implementation detail.

---

# Part A — Basic Statistics

Compute the following:

1. Sample mean
2. Sample variance
3. Sample standard deviation

Use `pressure_psi` as the target variable, and clearly report:

- sample size used,
- whether missing/duplicate records were removed,
- whether non-`NORMAL` statuses were included.

Then compare your empirical statistics with the assumed baseline `N(72, 4^2)` and comment on practical significance, not only numeric difference.

---

# Part B — Z-Scores

For each observation, compute the z-score using:

```text
z = (x - μ) / σ
```

Questions:
- Which values appear unusual?
- Does `81 psi` look like a potential outlier?

Also report:

- counts of observations with `|z| > 2` and `|z| > 3`,
- whether unusual values cluster in time,
- whether unusual values align with `sensor_status`, `pump_status`, or `anomaly_flag`.

---

# Part C — Probability Thinking

Assuming the original distribution is correct:

```text
X ~ N(72, 4²)
```

Estimate:

1. Probability that pressure exceeds `80 psi`
2. Probability that pressure falls below `65 psi`

You may use:
- z-tables,
- Python,
- SciPy,
- or approximation reasoning.

Then compare theoretical probabilities against empirical frequencies from the observed dataset (after your chosen cleaning strategy), and explain any meaningful mismatch.

---

# Part D — MCMC / Monte Carlo Connection

Suppose you do **not** know the true mean pressure anymore.

You now want to estimate the unknown system mean using simulation methods.

Conceptual Questions:

1. Why might Monte Carlo methods help here?
2. Why might sampling from a posterior distribution be useful?
3. What advantages would Bayesian estimation provide over a single-point estimate?

Expand your reasoning to account for real telemetry conditions:

- nonstationary periods,
- sensor reliability uncertainty,
- missing and duplicated records,
- possible mismatch between engineering assumptions and observed behavior.

---

# Part E — Infrastructure Engineering Interpretation

Assume:
- pressures above `80 psi` increase risk of pipe stress,
- pressures below `65 psi` increase risk of inadequate service.

Questions:
- Which condition is operationally more dangerous?
- Would occasional excursions matter?
- What additional data would you want before making engineering recommendations?

When answering, consider duration, frequency, and operational context (for example pump state and flow conditions), not only single-point exceedances.

---

# Bonus Mode — Monte Carlo Simulation

Implement a simple Monte Carlo simulation:

1. Generate `100,000` synthetic pressure readings
2. Estimate:
   - probability of exceeding `80 psi`,
   - expected pressure,
   - confidence intervals,
   - histogram behavior.

Then compare:
- analytical probability
vs
- simulated probability.

Also compare both against observed empirical probability from the dataset, and briefly discuss why the three values may differ.

Because eventually every sufficiently advanced infrastructure problem becomes:

> “We should probably simulate this 100,000 times and hope the pipes survive.”

---

# Suggested Python Libraries

You may optionally use:

```python
numpy
scipy
matplotlib
pandas
seaborn
```

Optional but useful additions (if you choose to extend beyond MVP):

```python
statsmodels
pymc
arviz
```

---

# Suggested Extensions

Possible future extensions include:

- Bayesian parameter estimation
- Posterior distribution visualization
- Markov Chain Monte Carlo sampling
- Time-series pressure analysis
- Infrastructure risk scoring
- Reliability modeling
- Sensor anomaly detection
- Predictive maintenance modeling
- Regime-shift detection and change-point analysis
- Reliability-weighted risk scoring

---

# Learning Objectives

This exercise introduces concepts related to:

- Probability distributions
- Descriptive statistics
- Standardization using z-scores
- Statistical inference
- Monte Carlo simulation
- Bayesian reasoning
- Infrastructure risk interpretation
- Engineering uncertainty

Additional practical objectives:

- data quality assessment under realistic telemetry conditions,
- communicating assumptions and uncertainty clearly,
- connecting statistical outputs to operational decisions.

The goal is not perfect model fit. The goal is defensible engineering interpretation under uncertainty.

---

# Deliverables

Suggested outputs:
- handwritten derivations,
- Jupyter notebook analysis,
- probability calculations,
- visualization plots,
- simulation results,
- engineering interpretation summary.

Include a short methods note describing:

- cleaning/validation steps,
- assumptions used in probability calculations,
- limitations of the analysis,
- what would be needed for production-level decision support.

If you produce multiple analysis variants (for example raw vs cleaned), summarize the differences and state which variant you trust most for engineering interpretation.

Because the real challenge in engineering is not producing numbers.

It is determining whether the numbers are quietly lying to you.