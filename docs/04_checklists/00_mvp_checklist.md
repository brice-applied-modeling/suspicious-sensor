# MVP Checklist — The Suspicious Sensor

**Last reviewed:** 2026-11-07  
**Branch:** `phase_1`  
**Reported test baseline:** 14/14 passing (not rerun for this revision)

## Phase Overview

| Phase | Focus | Notebook |
| --- | --- | --- |
| 1 | Data infrastructure and preprocessing | `notebooks/01_exploratory_data_analysis.ipynb` |
| 2 | Exploratory data analysis (Parts A–B) | `notebooks/01_exploratory_data_analysis.ipynb` |
| 3 | Probability analysis (Part C) | `notebooks/02_probability_analysis.ipynb` |
| 4 | Monte Carlo simulation (Bonus) | `notebooks/03_monte_carlo_simulation.ipynb` |
| 5 | Bayesian reasoning (Part D) | `notebooks/04_bayesian_estimation.ipynb` (optional implementation) |
| 6 | Engineering interpretation (Part E) | `notebooks/05_engineering_interpretation.ipynb` |
| 7 | Final validation and delivery | All required notebooks |

## Phase 1 — Data Infrastructure

### 1.1 Data Loading

**Module:** `src/suspicious_sensor/io/loader.py`

**Implementation**
- [x] Implement `load_data()`.
- [x] Handle invalid filename types and missing files.

**Unit Tests**
- [x] Test successful loading and DataFrame return type.
- [x] Test non-string filename raises `TypeError`.
- [x] Test missing file raises `FileNotFoundError`.

**Notebook**
- [x] Call `load_data()` in `notebooks/01_exploratory_data_analysis.ipynb` (originally under its previous filename).

### 1.2 Dataset Diagnostics

**Module:** `src/suspicious_sensor/diagnostics/diagnostics.py`

**Implementation**
- [x] Implement `dataset_diagnostics()`.
- [x] Report shape, data types, memory usage, and unique values.

**Unit Tests**
- [x] Test return type and expected result keys.
- [x] Test shape and data-type reporting.
- [x] Test memory usage and unique-value reporting.
- [x] Test empty DataFrame and invalid input handling.

**Notebook**
- [x] Call `dataset_diagnostics()` in `notebooks/01_exploratory_data_analysis.ipynb` (originally under its previous filename).
- [ ] Interpret diagnostic findings.

### 1.3 Dataset Validation

**Module:** `src/suspicious_sensor/diagnostics/validation.py`

**Implementation**
- [x] Implement DataFrame input type guard.
- [x] Return structured results (`structure`, `data_type`, `value_range`, `timestamp_validation`).
- [x] Implement timestamp parseability check.
- [ ] Update expected schema to `timestamp`, `pressure_psi`, `flow_gpm`, `sensor_status`, `pump_status`, `anomaly_flag`.
- [ ] Validate required, missing, and unexpected columns.
- [ ] Validate expected data types, allowing documented pre-conversion types.
- [ ] Validate pressure and flow ranges and missing values.
- [ ] Validate timestamp ordering, uniqueness, and hourly continuity.
- [ ] Validate allowed sensor/pump states and binary `anomaly_flag`.

**Unit Tests**
- [ ] Test valid schema and missing/extra columns.
- [ ] Test incorrect column types and invalid categorical values.
- [ ] Test invalid pressure/flow values and missing measurements.
- [ ] Test valid, unparseable, unordered, duplicated, and missing timestamps.
- [ ] Test empty DataFrame and non-DataFrame input.

**Notebook**
- [ ] Call `dataset_validation()` and present findings in `notebooks/01_exploratory_data_analysis.ipynb`.

### 1.4 Missing Data

**Module:** `src/suspicious_sensor/preprocessing/data_cleaning.py` (or existing location of investigation functions)

**Implementation**
- [x] Implement `missing_data_investigation()`.
- [x] Implement `summarize_missing_data()`.
- [ ] Implement an explicit pressure-analysis filtering policy for missing / `OFFLINE` readings.
- [ ] Retain excluded records for sensor-reliability summaries.

**Unit Tests**
- [ ] Test missing-value counts and percentages.
- [ ] Test missingness grouped by sensor and pump status.
- [ ] Test filtering behavior and preservation of non-pressure records.
- [ ] Test no-missing-data and all-missing-pressure cases.

**Notebook**
- [x] Call `missing_data_investigation()` in `notebooks/01_exploratory_data_analysis.ipynb` (originally under its previous filename).
- [ ] Replace duplicated inline missing-data logic with reusable functions where appropriate.
- [ ] Compare record counts before and after filtering.

**Methods Documentation**
- [x] Record missing-pressure findings in `docs/05_lessons_learned/02_lessons_learned_missing_pressure_data.md`.
- [ ] Record the chosen exclusion/imputation policy and its analytical consequences in the EDA notebook.

### 1.5 Duplicate Records

**Module:** `src/suspicious_sensor/preprocessing/data_cleaning.py`

**Implementation**
- [x] Implement `duplicate_rows_summary()`.
- [x] Implement `duplicate_rows_details()`.
- [x] Implement `drop_duplicate_rows()`.
- [ ] Consolidate `duplicate_rows_details()` and `get_duplicate_rows()`.
- [ ] Distinguish all members of duplicate groups from excess rows removed.
- [ ] Define treatment of identical rows versus conflicting duplicate timestamps.

**Unit Tests**
- [ ] Test no duplicates, identical duplicates, and conflicting timestamps.
- [ ] Test duplicate counts under the documented counting convention.
- [ ] Test removal preserves expected records and does not modify the input unexpectedly.
- [ ] Test empty DataFrame handling.

**Notebook**
- [ ] Report duplicate-row and duplicate-timestamp findings.
- [ ] Apply and explain the selected duplicate policy.

### 1.6 Type Conversion and Preprocessing

**Module:** `src/suspicious_sensor/preprocessing/data_cleaning.py`

**Implementation**
- [ ] Implement timestamp conversion to datetime.
- [ ] Implement appropriate numeric/categorical conversions.
- [ ] Preserve raw data and define a reproducible cleaned analytical dataset.

**Unit Tests**
- [ ] Test valid and invalid timestamp conversion.
- [ ] Test expected converted dtypes and missing-value preservation.
- [ ] Test invalid categorical/numeric inputs and non-mutation where required.

**Notebook**
- [ ] Apply preprocessing in a documented order.
- [ ] Report raw versus cleaned record counts and exclusions.

**Methods Documentation**
- [ ] Record material preprocessing decisions and their rationale in `notebooks/01_exploratory_data_analysis.ipynb`.

### 1.7 Phase 1 Verification

- [ ] Run Phase 1 unit tests successfully.
- [ ] Add integration test for load → validate → preprocess using representative data.
- [ ] Confirm `data/raw/pressure_sensor_readings.csv` remains unchanged.
- [ ] Confirm notebook imports and preprocessing cells run from a fresh kernel.

---

## Phase 2 — Exploratory Data Analysis (Parts A–B)

**Notebook:** `notebooks/01_exploratory_data_analysis.ipynb`

### 2.1 Descriptive Statistics (Part A)

**Implementation — `src/suspicious_sensor/statistics/`**
- [ ] Compute sample size, mean, sample variance (`ddof=1`), and sample standard deviation.
- [ ] Compare results with baseline μ = 72 psi and σ = 4 psi.
- [ ] Compare relevant raw and cleaned populations and sensor operating states.

**Unit Tests**
- [ ] Test known-value mean, sample variance, and sample standard deviation.
- [ ] Test missing values, empty input, and insufficient sample size.

**Notebook**
- [ ] Present statistics, sample definitions, and practical interpretation.

### 2.2 Visualization and Time-Series Exploration

**Implementation / Notebook**
- [ ] Plot pressure histogram with `N(72, 4²)` overlay.
- [ ] Plot box plot and distribution diagnostics (KDE / Q-Q as appropriate).
- [ ] Plot pressure time series and rolling mean/standard deviation.
- [ ] Examine pressure by `sensor_status` and `pump_status` and against `flow_gpm`.
- [ ] Highlight anomalous periods and explain relevant patterns.

**Unit Tests**
- [ ] Test any extracted plotting or rolling-statistics functions with meaningful edge cases.

### 2.3 Z-Scores and Outliers (Part B)

**Implementation — `src/suspicious_sensor/statistics/`**
- [ ] Implement baseline z-score calculation using μ = 72, σ = 4.
- [ ] Count observations with `|z| > 2` and `|z| > 3`.
- [ ] Examine temporal clustering and alignment with status, pump operation, and `anomaly_flag`.

**Unit Tests**
- [ ] Test known z-scores, threshold counts, missing values, and zero standard deviation.

**Notebook**
- [ ] Evaluate whether 81 psi is unusual under the baseline.
- [ ] Interpret outliers in operational context.

### 2.4 Phase 2 Verification

- [ ] Run relevant unit tests successfully.
- [ ] Run `notebooks/01_exploratory_data_analysis.ipynb` from a fresh kernel.
- [ ] Document analytical populations, assumptions, findings, and limitations in the notebook.

---

## Phase 3 — Probability Analysis (Part C)

**Notebook:** `notebooks/02_probability_analysis.ipynb`

### 3.1 Probability Calculations

**Implementation — `src/suspicious_sensor/statistics/`**
- [ ] Compute theoretical `P(X > 80)` and `P(X < 65)` for `X ~ N(72, 4²)` using SciPy.
- [ ] Compute empirical frequencies for defined analytical populations.
- [ ] Calculate absolute differences between theoretical and empirical probabilities.

**Unit Tests**
- [ ] Test theoretical calculations against known normal-distribution values.
- [ ] Test empirical frequencies with known data, missing values, and empty samples.
- [ ] Test strict threshold behavior (`>` versus `<`).

### 3.2 Notebook Analysis

- [ ] Present equations, assumptions, and comparison table.
- [ ] Explain differences arising from operating regimes, sensor faults, or baseline mismatch.
- [ ] Address time dependence when interpreting observed frequencies.

### 3.3 Phase 3 Verification

- [ ] Run relevant unit tests successfully.
- [ ] Run notebook from a fresh kernel.
- [ ] Document conclusions and limitations in the notebook.

---

## Phase 4 — Monte Carlo Simulation (Bonus)

**Notebook:** `notebooks/03_monte_carlo_simulation.ipynb`

### 4.1 Simulation

**Implementation — `src/suspicious_sensor/simulation/`**
- [ ] Implement `run_monte_carlo()` or equivalent reusable simulation function.
- [ ] Generate 100,000 draws from `N(72, 4²)` using a fixed random seed.
- [ ] Estimate mean pressure and `P(X > 80)`.
- [ ] Define and compute an appropriate 95% confidence interval, stating the estimand.
- [ ] Examine estimate convergence with increasing simulation size.

**Unit Tests**
- [ ] Test output size, type, and valid parameter handling.
- [ ] Test deterministic reproducibility with the same seed.
- [ ] Test invalid sample sizes and distribution parameters.
- [ ] Test estimates against analytical expectations within justified tolerances.

### 4.2 Notebook Analysis

- [ ] Plot simulated histogram with baseline distribution overlay.
- [ ] Compare analytical, simulated, and observed exceedance probabilities.
- [ ] Explain simulation error versus model-assumption uncertainty.
- [ ] Interpret differences for engineering decision-making.

### 4.3 Phase 4 Verification

- [ ] Run relevant unit tests successfully.
- [ ] Run notebook from a fresh kernel.
- [ ] Record simulation assumptions, seed, sample size, findings, and limitations in the notebook.

---

## Phase 5 — Bayesian Reasoning (Part D)

**Conceptual discussion required; numerical Bayesian implementation optional.**  
**Optional notebook:** `notebooks/04_bayesian_estimation.ipynb`

### 5.1 Required Conceptual Analysis

- [ ] Explain why Monte Carlo methods may help when true mean pressure is unknown.
- [ ] Explain posterior sampling and how it differs from baseline simulation.
- [ ] Explain advantages and limitations of Bayesian estimates versus point estimates.
- [ ] Address nonstationarity, sensor reliability, missing data, duplicates, and autocorrelation.
- [ ] Include conclusions in `notebooks/05_engineering_interpretation.ipynb` if no Bayesian notebook is implemented.

### 5.2 Optional Bayesian Implementation

**Implementation — `src/suspicious_sensor/models/`**
- [ ] Define prior, likelihood, and analytical population.
- [ ] Implement posterior estimation (conjugate update or MCMC).
- [ ] Compute posterior summaries and credible intervals.
- [ ] Assess prior and preprocessing sensitivity.

**Unit Tests**
- [ ] Test posterior calculations on known synthetic cases.
- [ ] Test input validation and edge cases.
- [ ] Test reproducibility and sampling diagnostics if MCMC is used.

**Notebook**
- [ ] Present posterior results, diagnostics, assumptions, and interpretation.

---

## Phase 6 — Engineering Interpretation (Part E)

**Notebook:** `notebooks/05_engineering_interpretation.ipynb`

### 6.1 Excursion and Operational Risk Analysis

**Implementation — `src/suspicious_sensor/statistics/` or appropriate existing module**
- [ ] Calculate frequency and duration of excursions above 80 psi and below 65 psi.
- [ ] Summarize excursion episodes by sensor state, pump state, and flow context.
- [ ] Distinguish probable sensor artifacts from plausible operating events.

**Unit Tests**
- [ ] Test excursion thresholds and episode counts with known sequences.
- [ ] Test duration calculations with gaps, duplicates, and missing readings.
- [ ] Test no-excursion and all-excursion cases.

### 6.2 Notebook Synthesis

- [ ] Summarize findings from EDA, probability analysis, and Monte Carlo simulation.
- [ ] Evaluate relative significance of high- and low-pressure events.
- [ ] Discuss whether occasional excursions matter and under what conditions.
- [ ] State whether evidence supports the original `N(72, 4²)` assumption.
- [ ] Identify additional operational data needed before engineering recommendations.
- [ ] State limitations and recommended next investigations.

### 6.3 Phase 6 Verification

- [ ] Run relevant unit tests successfully.
- [ ] Run notebook from a fresh kernel.
- [ ] Confirm interpretations are supported by calculated results.

---

## Phase 7 — Final Validation and Delivery

### 7.1 Code and Testing

- [ ] Run complete unit test suite successfully.
- [ ] Run integration tests successfully.
- [ ] Confirm all reusable functions have accurate docstrings and appropriate type hints.
- [ ] Confirm dependencies are declared in `pyproject.toml` and resolved in `uv.lock`.

### 7.2 Notebooks and Data

- [ ] Execute all required notebooks from clean kernels in sequence.
- [ ] Confirm no notebook depends on hidden state from another notebook.
- [ ] Verify outputs, figures, units, and dataset population labels.
- [ ] Confirm reproducibility of random simulations.
- [ ] Preserve raw data and document any processed outputs.

### 7.3 Project Documentation

- [ ] Update `README.md` with project purpose, setup, execution order, and key findings.
- [ ] Ensure `docs/01_architecture/01_structure.md` reflects the actual repository.
- [ ] Record material design and preprocessing decisions in the relevant architecture documents or notebooks.
- [ ] Include a concise methods and limitations summary.
- [ ] Export final required notebooks to PDF if needed for portfolio delivery.

### 7.4 Release Readiness

- [ ] Review Git changes and remove temporary outputs or unused code.
- [ ] Verify all required Parts A–E and the Monte Carlo bonus are addressed.
- [ ] Confirm checklist completion against actual files and test results.

---

## Post-MVP Extensions

- [ ] `notebooks/06_anomaly_detection.ipynb` — statistical and ML detection using `anomaly_flag` for evaluation.
- [ ] `notebooks/07_time_series_modeling.ipynb` — temporal dependence, regime changes, and change-point analysis.
- [ ] `notebooks/08_reliability_risk_modeling.ipynb` — reliability and operational risk modeling.
- [ ] Predictive maintenance modeling, if supported by suitable data and targets.
