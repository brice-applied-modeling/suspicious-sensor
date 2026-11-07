# Notebook Management Strategy

## Purpose

This guide establishes consistent practices for developing, organizing, validating, and maintaining Jupyter notebooks in the Suspicious Sensor project. Notebooks are reproducible analytical reports, not substitutes for reusable application modules.

## Roles and Boundaries

| Location | Responsibility |
| --- | --- |
| `../../../../notebooks` | Exploratory analysis, presentation of results, plots, assumptions, and engineering interpretation |
| `../../../../src/suspicious_sensor/io` | Reusable data loading |
| `../../../../src/suspicious_sensor/diagnostics` | Diagnostics and validation |
| `../../../../src/suspicious_sensor/preprocessing` | Cleaning and transformations |
| `../../../../src/suspicious_sensor/statistics` | Reusable statistical calculations |
| `../../../../src/suspicious_sensor/models` | Reusable anomaly-detection and estimation models |
| `../../../../src/suspicious_sensor/simulation` | Reusable simulation logic |
| `../../../../src/suspicious_sensor/visualization` | Reusable plotting logic where warranted |
| `../../../../tests/unit_tests` | Tests for application functions |

Simple, transparent one-line exploratory operations may remain in notebooks. Extract code when it is reused, requires substantial validation, or represents a stable analytical operation. Avoid creating utility functions solely to wrap basic pandas operations.

## Notebook Organization

Use descriptive, ordered filenames (`NN_short_topic.ipynb`). The existing notebook is `01_descriptive_statistics.ipynb`. Additional notebooks should be created only when they represent distinct analytical questions, rather than splitting work arbitrarily. The standard suite below is a recommended structure, not a list of committed deliverables; create each notebook only when its question is being actively worked.

## Standard Notebook Suite

The suite follows the usual analytical lifecycle: **audit → explore → baseline → model → simulate → interpret**. Each notebook should consume the outputs or conclusions of earlier notebooks rather than repeating their work.

| # | Notebook | Lifecycle role | Problem statement coverage | Status |
| --- | --- | --- | --- | --- |
| 00 | `00_data_audit.ipynb` | Data quality / validation | Data context and preprocessing decisions | Proposed (currently covered in `01`) |
| 01 | `01_descriptive_statistics.ipynb` | EDA | Parts A and B | Exists |
| 02 | `02_baseline_probability.ipynb` | Baseline | Part C | Proposed |
| 03 | `03_anomaly_model.ipynb` | Model | Extension beyond MVP | Proposed (optional) |
| 04 | `04_monte_carlo_simulation.ipynb` | Simulation | Bonus | Proposed |
| 05 | `05_bayesian_estimation.ipynb` | Model (uncertainty) | Part D | Proposed (optional) |
| 06 | `06_engineering_interpretation.ipynb` | Reporting | Part E and final synthesis | Proposed |
| 99 | `99_scratch_*.ipynb` | Scratch | None | Not committed |

### 00 — Data Audit (`00_data_audit.ipynb`)

**Question:** Is the raw dataset fit for analysis, and what cleaning decisions are required?

Include:

- Schema check: column names, dtypes, timestamp parsing, and expected record count (~4,340).
- Missing values by column, with `pressure_psi` gaps cross-tabulated against `sensor_status` (e.g., `OFFLINE`).
- Duplicate rows and duplicate timestamps: counts, examples, and whether duplicates are identical or conflicting.
- Time-index continuity: gaps or irregular intervals in the hourly series.
- Categorical value counts for `sensor_status`, `pump_status`, and `anomaly_flag`.
- Range and plausibility checks (negative or physically impossible pressure/flow values).
- Telemetry artifacts such as frozen (repeated) values and abrupt step changes.
- A **cleaning decision log**: each rule, its justification, and the number of rows affected.
- Output: optionally a cleaned dataset in `data/processed/`, with its creation documented.

Use the functions in `diagnostics/` and `preprocessing/`; the notebook presents and explains their results. While the audit remains small, it can stay as an opening section of `01`; split it out once it becomes a standalone deliverable.

### 01 — Exploratory Data Analysis / Descriptive Statistics (`01_descriptive_statistics.ipynb`)

**Question:** What does the observed pressure behavior look like, and how does it compare with the assumed `N(72, 4²)`?

Include:

- Sample mean, variance, and standard deviation, reporting sample size and raw vs. cleaned basis (Part A).
- Comparison of empirical statistics with the baseline assumption, with discussion of practical significance.
- Distribution plots: histogram with an overlaid `N(72, 4²)` density, box plot, and Q-Q plot.
- Time-series plot of `pressure_psi` with injected-event periods, sensor states, and pump states visible.
- Grouped summaries by `sensor_status` and `pump_status`; pressure-flow relationship.
- Z-scores, `|z| > 2` and `|z| > 3` counts, the `81 psi` question, and temporal clustering of unusual values (Part B).
- Alignment of unusual values with `anomaly_flag`, used for comparison only.

Follow the ten-section outline in `../../01_descriptive_statistics_strategy.md`.

### 02 — Baseline (`02_baseline_probability.ipynb`)

**Question:** Assuming the original engineering model is correct, what should we expect, and how does reality differ?

The baseline is the reference that every later model must beat or explain. Include:

- Statement of the baseline model: `X ~ N(72, 4²)` and the `80 psi` / `65 psi` thresholds.
- Theoretical probabilities `P(X > 80)` and `P(X < 65)` computed with SciPy, plus a z-table cross-check.
- Empirical exceedance frequencies from the cleaned data (and raw, if the difference is informative).
- A comparison table: theoretical vs. empirical, with absolute and relative differences.
- Simple baseline anomaly rules (fixed thresholds and `|z| > 3`) evaluated against `anomaly_flag` (confusion matrix, precision, and recall). These are the benchmark scores for notebook `03`.
- Discussion of why mismatches occur: nonstationarity, drift, sensor faults, or an incorrect mean/variance.

### 03 — Anomaly Model (`03_anomaly_model.ipynb`, optional)

**Question:** Can a context-aware method identify abnormal periods better than the baseline rules?

Include:

- Model candidates appropriate to the data, such as rolling-window z-scores, change-point detection, frozen-value detection, or pump-state-conditioned thresholds.
- Feature definitions (rolling mean/std, rate of change, flow context), implemented in `../../../../src` and tested.
- A time-aware evaluation design: avoid random splits that leak adjacent hourly records.
- Metrics against `anomaly_flag`, reported alongside the baseline scores from `02`.
- Error analysis: which event types (high/low excursions, drift, frozen values) are missed or falsely flagged.
- Justification for the chosen method, including its interpretability for operators.

Model logic belongs in `../../../../src/suspicious_sensor/models`; the notebook handles configuration, evaluation, and interpretation.

### 04 — Monte Carlo Simulation (`04_monte_carlo_simulation.ipynb`)

**Question:** Do simulated results agree with analytical and observed probabilities?

Include:

- Simulation settings: distribution, parameters, sample size (`100,000`), and a fixed random seed.
- Simulated `P(X > 80)`, expected pressure, and confidence intervals.
- Histogram of simulated readings with the analytical density overlaid.
- A convergence check showing how the estimate stabilizes as sample size grows.
- A three-way comparison table: analytical vs. simulated vs. observed.
- An optional scenario that simulates with parameters estimated from the observed data, to show the effect of model mismatch.
- Discussion that separates Monte Carlo sampling error from uncertainty in the model assumptions.

Simulation functions belong in `../../../../src/suspicious_sensor/simulation`.

### 05 — Bayesian Estimation (`05_bayesian_estimation.ipynb`, optional)

**Question:** If the true mean is unknown, what range of values is credible?

Part D is primarily conceptual, so its answers may live in `06` as written discussion. Create this notebook only if implementing an estimate. Include:

- Prior choice (e.g., centered on 72 psi) and its justification.
- Likelihood assumptions and their known violations (autocorrelation, nonstationarity).
- Posterior via a conjugate update or simple MCMC sampler, with trace and convergence diagnostics.
- Posterior mean and credible interval compared with the frequentist point estimate and confidence interval.
- Sensitivity analysis to the prior and to the cleaning strategy.

### 06 — Engineering Interpretation (`06_engineering_interpretation.ipynb`)

**Question:** What do the findings mean for the utility, and what should be done next?

This is the reporting notebook; it should contain minimal new computation. Include:

- An executive summary of findings from notebooks `00`–`05`.
- Excursion analysis: frequency, duration, and timing of events above `80 psi` and below `65 psi`, with pump and flow context.
- Comparison of risk between high and low pressure conditions (Part E).
- Answers to the Part D conceptual questions if `05` was not created.
- A conclusion on whether the system remains consistent with the original assumptions.
- Recommendations, additional data needs, and limitations.
- Key figures suitable for PDF export and the Power BI dashboard (`03_dashboard/00_power_bi_dashboard_plan.md`).

### 99 — Scratch Notebooks (`99_scratch_*.ipynb`)

Use scratch notebooks for quick experiments. Do not commit them (or keep them gitignored), and do not let other notebooks depend on them. Promote useful findings to the appropriate numbered notebook.

## Standard Notebook Sections

For each numbered notebook, include:

1. **Title and objective**: What engineering question is being answered?
2. **Dataset and assumptions**: Data source, baseline assumptions, and known limitations.
3. **Imports and setup**: Dependencies and reproducibility settings.
4. **Data loading**: Call the project loader rather than duplicating file-path logic.
5. **Inspection and validation**: Establish data quality before relying on results.
6. **Analysis**: Present calculations and plots in a logical sequence.
7. **Interpretation**: Explain what findings mean operationally, not just numerically.
8. **Limitations and next steps**: Identify unresolved issues and decisions.

The descriptive statistics notebook already has a ten-section plan in `../../01_descriptive_statistics_strategy.md`; follow that specific outline where applicable.

## Cell-Level Practices

- Start each major section with a Markdown heading and a short explanation of its purpose.
- Keep code cells focused on one analytical step or tightly related steps.
- Use descriptive variable names; clarity matters more than minimizing line count.
- Display relevant outputs deliberately. Avoid large, unexplained DataFrame dumps.
- Place interpretation immediately after important tables or figures.
- Explain decisions about missing values, duplicates, sensor states, and pressure excursions.
- Distinguish observed evidence from assumptions and engineering judgment.
- Avoid hidden state: do not rely on variables defined only by running cells out of order.

## Recommended Development Workflow

1. Identify the analytical question and expected output.
2. Inspect the dataset and document relevant quality concerns.
3. Prototype the smallest calculation or visualization in the notebook.
4. Decide whether the logic is notebook-specific or reusable.
5. If reusable, move the logic to the appropriate `../../../../src/suspicious_sensor` module.
6. Write focused unit tests for that module, including meaningful edge cases.
7. Import and call the tested function from the notebook.
8. Explain the result and its engineering significance in Markdown.
9. Restart the kernel and run all cells from top to bottom.
10. Review outputs, assumptions, and reproducibility before committing changes.

## Data Handling

- Keep `../../../../data/raw` unchanged.
- Store derived datasets under `data/processed/` when necessary.
- Clearly label whether each result uses raw data, cleaned data, or both.
- Document cleaning criteria, especially missing pressures, duplicate timestamps, non-`NORMAL` sensor states, and telemetry artifacts.
- Do not use `anomaly_flag` as a substitute for independent anomaly reasoning; use it for subsequent validation or comparison.

## Testing and Validation

**Unit tests:** Test functions in `../../../../src` with pytest. Prefer small synthetic DataFrames for focused cases; use the project dataset for a limited number of integration-style checks.

**Notebook checks:** Confirm imports work in the configured environment, cells execute sequentially after a kernel restart, outputs are consistent with stated assumptions, and no stale outputs contradict the current code.

**Simulation checks:** Fix random seeds where appropriate, record simulation settings and sample sizes, and distinguish Monte Carlo variability from uncertainty in model assumptions.

## Reproducibility and Version Control

- Use the project's `../../../../pyproject.toml` and `uv.lock` to maintain a reproducible environment.
- Do not embed machine-specific absolute paths or secrets in notebooks.
- Avoid committing unnecessary large outputs or generated datasets.
- Review notebook diffs for accidental output churn before committing.
- Export a notebook to PDF when required by the MVP checklist, after verifying its outputs.

## Descriptive Statistics Notebook Checklist

- [ ] Notebook objective and data source documented
- [ ] Imports and data loading work from a clean kernel
- [ ] Dataset diagnostics presented and explained
- [ ] Validation and cleaning decisions recorded
- [ ] Descriptive statistics calculated and interpreted
- [ ] Distribution and time-series figures labeled and interpreted
- [ ] Z-score and outlier findings explained
- [ ] Engineering implications and limitations documented
- [ ] Reusable functions extracted and unit-tested where appropriate
- [ ] All cells run top-to-bottom without errors
- [ ] Final notebook reviewed and exported as needed

## Relationship to Other Project Documents

- `../../00_strategy_overview.md`: high-level component responsibilities.
- `../../01_descriptive_statistics_strategy.md`: specific analytical sequence and scope.
- `00_mvp_checklist.md`: tracks implementation and deliverable completion.
- `01_structure.md`: documents repository layout.

This document governs notebook working practices; it does not replace the analytical strategy or project checklist.
