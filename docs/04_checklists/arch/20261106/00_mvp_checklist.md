# MVP Checklist — The Suspicious Sensor

This checklist tracks the minimum deliverables required to complete the core analysis
defined in the problem statement. Items are organized by phase, mirroring the notebook
structure and utility component strategy.

_Last reviewed: 2026-11-07 (branch `phase_1`, 14/14 tests passing)_

---

## Phase 1 — Data Infrastructure

### Data Loading (`io/loader.py`)
- [x] `load_data()` utility function implemented
- [x] `load_data()` unit tests written and passing (returns DataFrame, `TypeError` on non-string, `FileNotFoundError`)

### Dataset Diagnostics (`diagnostics/diagnostics.py` → `dataset_diagnostics()`)
- [x] Implement shape reporting
- [x] Implement data type inspection
- [x] Implement memory usage reporting
- [x] Implement unique value counts (all columns, incl. `sensor_status`, `pump_status`, `anomaly_flag`)
- [x] Unit tests written and passing (8 tests: return type, keys, shape, dtypes, memory, unique values, empty df, invalid input)

### Dataset Validation (`diagnostics/validation.py` → `dataset_validation()`)
> **Status:** scaffold only. The function currently expects `timestamp`, `sensor_id`,
> `pressure_reading`, but the dataset columns are `timestamp`, `pressure_psi`, `flow_gpm`,
> `sensor_status`, `pump_status`, `anomaly_flag`. Run against the real data, it reports
> `sensor_id` and `pressure_reading` as missing and every real column as "extra".

- [x] Input type guard (`TypeError` on non-DataFrame)
- [x] Return a structured results dictionary (`structure`, `data_type`, `value_range`, `timestamp_validation`)
- [ ] Update expected schema to match the actual dataset columns
- [ ] Validate expected columns are present and correctly named (missing/extra detection exists, but uses the wrong schema)
- [ ] Validate column data types against expected types (timestamp → datetime, pressure_psi → float, etc.) — currently only *reports* dtypes
- [ ] Validate value ranges (pressure_psi: non-negative, realistic bounds) — currently only reports min/max of a nonexistent column
- [x] Validate timestamp parseability (`timestamp_format`)
- [ ] Validate timestamp ordering (monotonic increasing)
- [ ] Validate timestamp uniqueness
- [ ] Validate timestamp completeness (no gaps in the expected hourly cadence)
- [ ] Validate categorical values against allowed sets (`sensor_status`, `pump_status`, `anomaly_flag` ∈ {0, 1})
- [ ] Unit tests written and passing

### Data Cleaning (`preprocessing/data_cleaning.py`)

**Missing values**
- [x] Missing value investigation implemented (`missing_data_investigation()` — by sensor status, pump status, time clustering, risk note)
- [x] Missing value summary implemented (`summarize_missing_data()`)
- [x] Missingness findings documented (`../../../05_lessons_learned/02_lessons_learned_missing_pressure_data.md`)
- [ ] Missing value handling implemented (e.g., exclude `OFFLINE` / NaN pressure rows from pressure statistics while retaining them for reliability analysis)
- [ ] Unit tests written and passing

**Duplicates**
- [x] Duplicate row summary implemented (`duplicate_rows_summary()`)
- [x] Duplicate row details implemented (`duplicate_rows_details()`)
- [x] Duplicate record removal implemented (`drop_duplicate_rows()`)
- [ ] Consolidate `duplicate_rows_details()` and `get_duplicate_rows()` (identical implementations)
- [ ] Clarify `duplicate_count` semantics — uses `keep=False`, so it counts *all* copies (originals + duplicates), not the number of rows `drop_duplicate_rows()` will remove
- [ ] Unit tests written and passing

**Type conversion**
- [ ] Timestamp parsing and conversion implemented (`timestamp` currently loads as string dtype)
- [ ] Data type conversion utility implemented (categoricals, `anomaly_flag` → int/bool)

### Notebook Integration
- [x] `load_data()`, `dataset_diagnostics()`, and `missing_data_investigation()` called from `01_descriptive_statistics.ipynb`
- [ ] `dataset_validation()` called from the notebook
- [ ] Duplicate and type-conversion utilities called from the notebook
- [ ] Inline missing-value logic in the notebook replaced with utility calls

---

## Phase 2 — Descriptive Statistics (Problem Part A)

- [ ] Sample mean computed for `pressure_psi`
- [ ] Sample variance computed for `pressure_psi`
- [ ] Sample standard deviation computed for `pressure_psi`
- [ ] `compute_descriptive_stats()` utility function extracted to `src/suspicious_sensor/statistics`
- [ ] Results compared against assumed distribution (μ=72, σ=4)

---

## Phase 3 — Z-Score Analysis (Problem Part B)

- [ ] Z-score computed for each observation using assumed μ=72, σ=4
- [ ] `compute_z_scores()` utility function extracted to `src/suspicious_sensor/statistics`
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
- [ ] `run_monte_carlo()` utility function extracted to `src/suspicious_sensor/simulation`

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
- [ ] All utility calls reference `src/suspicious_sensor` (no inline logic duplication)
- [ ] Markdown cells provide narrative explanation for each section
- [ ] Notebook exported to PDF (final version — current `notebooks/01_descriptive_statistics.pdf` is an early draft)

---

## Stretch Goals (Post-MVP)

- [ ] Conceptual writeup: why Monte Carlo helps when the true mean is unknown (Part D)
- [ ] Bayesian parameter estimation notebook
- [ ] Posterior distribution visualization
- [ ] MCMC sampling implementation
- [ ] Sensor anomaly detection using `anomaly_flag` ground truth
- [ ] Infrastructure risk scoring model
- [ ] Predictive maintenance modeling
