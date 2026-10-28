# MVP Checklist — The Suspicious Sensor

This checklist tracks the minimum deliverables required to complete the core analysis
defined in the problem statement. Items are organized by phase, mirroring the notebook
structure and utility component strategy.

---

## Phase 1 — Data Infrastructure

### Data Loading
- [x] `load_data()` utility function implemented
- [ ] `load_data()` unit test written and passing

### Dataset Diagnostics (`dataset_diagnostics()`)
- [x] Implement shape reporting
- [x] Implement data type inspection
- [x] Implement memory usage reporting
- [x] Implement unique value counts for categorical columns (`sensor_status`, `pump_status`, `anomaly_flag`)
- [ ] Unit test written and passing

### Dataset Validation (`dataset_validation()`)
- [x] Validate expected columns are present and correctly named
- [x] Validate column data types (timestamp → datetime, pressure_psi → float, etc.)
- [x] Validate value ranges (pressure_psi: non-negative, realistic bounds)
- [x] Validate timestamp ordering, uniqueness, and completeness
- [ ] Unit test written and passing

### Data Cleaning
- [ ] Missing value handling utility implemented
- [ ] Timestamp parsing and conversion implemented
- [ ] Duplicate record removal implemented
- [ ] Data type conversion utility implemented

---

## Phase 2 — Descriptive Statistics (Problem Part A)

- [ ] Sample mean computed for `pressure_psi`
- [ ] Sample variance computed for `pressure_psi`
- [ ] Sample standard deviation computed for `pressure_psi`
- [ ] `compute_descriptive_stats()` utility function extracted to `src/utils/`
- [ ] Results compared against assumed distribution (μ=72, σ=4)

---

## Phase 3 — Z-Score Analysis (Problem Part B)

- [ ] Z-score computed for each observation using assumed μ=72, σ=4
- [ ] `compute_z_scores()` utility function extracted to `src/utils/`
- [ ] Unusual values identified and flagged
- [ ] 81 psi observation investigated as a potential outlier

---

## Phase 4 — Probability Analysis (Problem Part C)

- [ ] P(pressure > 80 psi) estimated under assumed distribution
- [ ] P(pressure < 65 psi) estimated under assumed distribution
- [ ] SciPy `norm` used for analytical calculation
- [ ] Results documented with interpretation

---

## Phase 5 — Visualizations

- [ ] Histogram of `pressure_psi` with reference distribution overlay
- [ ] Box plot of `pressure_psi`
- [ ] Distribution plot (KDE) of `pressure_psi`
- [ ] Time series plot of `pressure_psi` over monitoring period
- [ ] Rolling mean and rolling standard deviation plotted
- [ ] Anomaly-flagged observations highlighted on time series
- [ ] All plots use consistent style and axis labels

---

## Phase 6 — Monte Carlo Simulation (Problem Bonus)

- [ ] Generate 100,000 synthetic pressure readings from N(72, 4²)
- [ ] Estimate P(pressure > 80 psi) from simulation
- [ ] Estimate expected pressure from simulation
- [ ] Compute 95% confidence interval from simulation
- [ ] Plot simulated histogram vs. observed distribution
- [ ] Compare analytical probability vs. simulated probability
- [ ] `run_monte_carlo()` utility function extracted to `src/utils/`

---

## Phase 7 — Engineering Interpretation (Problem Part E)

- [ ] Determine which condition is operationally more dangerous (high vs. low pressure)
- [ ] Assess operational significance of occasional pressure excursions
- [ ] Identify what additional data would be needed for engineering recommendations
- [ ] Summarize findings in a written interpretation cell in the notebook

---

## Phase 8 — Notebook Completeness

- [ ] Notebook `01_descriptive_statistics.ipynb` follows the 10-section structure from strategy doc
- [ ] All cells execute top-to-bottom without error
- [ ] All utility calls reference `src/utils/` (no inline logic duplication)
- [ ] Markdown cells provide narrative explanation for each section
- [ ] Notebook exported to PDF

---

## Stretch Goals (Post-MVP)

- [ ] Conceptual writeup: why Monte Carlo helps when the true mean is unknown (Part D)
- [ ] Bayesian parameter estimation notebook
- [ ] Posterior distribution visualization
- [ ] MCMC sampling implementation
- [ ] Sensor anomaly detection using `anomaly_flag` ground truth
- [ ] Infrastructure risk scoring model
- [ ] Predictive maintenance modeling
