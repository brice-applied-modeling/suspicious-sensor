# Notebook Management Strategy

## Purpose

This guide establishes consistent practices for developing, organizing, validating, and maintaining Jupyter notebooks in the **Suspicious Sensor** project. The primary investigation is a probability, statistics, and Monte Carlo study of synthetic water-infrastructure telemetry. Notebooks are reproducible analytical reports, not substitutes for reusable Python modules.

The organizational goal is **one notebook per meaningful analytical stage**, not one notebook per individual calculation. The project begins with exploratory data analysis (EDA), progresses through probability analysis and simulation, and concludes with defensible engineering interpretation. Bayesian implementation and machine learning are valuable expansions, but are not prerequisites for completing the original exercise.

## Roles and Boundaries

| Location | Responsibility |
| --- | --- |
| `notebooks/` | Exploratory analysis, plots, assumptions, results, and engineering interpretation |
| `src/suspicious_sensor/io/` | Reusable data loading |
| `src/suspicious_sensor/diagnostics/` | Data diagnostics and validation |
| `src/suspicious_sensor/preprocessing/` | Cleaning, filtering, and transformations |
| `src/suspicious_sensor/statistics/` | Reusable statistical and probability calculations |
| `src/suspicious_sensor/models/` | Reusable estimation and optional anomaly-detection models |
| `src/suspicious_sensor/simulation/` | Reusable simulation logic |
| `src/suspicious_sensor/visualization/` | Reusable plotting logic where warranted |
| `tests/unit_tests/` | Focused tests of reusable functions |
| `data/raw/` | Original data, never modified in place |
| `data/processed/` | Documented analytical datasets when needed |
| `docs/` | Problem statement, strategies, methods, and architecture |

Simple exploratory operations such as `df.shape` and `df.describe()` may remain in notebooks. Extract code when it is reused, requires meaningful validation, or represents a stable analytical operation. Avoid wrappers around trivial pandas expressions.

**Architecture note:** The paths above reflect the package structure in this management strategy. If the repository still uses a legacy `src/utils/` layout, confirm the actual structure before changing imports or moving files. This document does not itself require an immediate refactor.

## Notebook Organization

Use ordered, descriptive filenames (`NN_short_topic.ipynb`). The existing `01_descriptive_statistics.ipynb` can be renamed to `01_exploratory_data_analysis.ipynb` when convenient. Retain the existing notebook and its work; do not recreate it from scratch.

### Core Notebook Suite

| # | Notebook | Primary analytical question | Problem statement | Status |
| --- | --- | --- | --- | --- |
| 01 | `01_exploratory_data_analysis.ipynb` | What data can be trusted, and how does pressure behave? | Data context; Parts A and B | In progress; currently named `01_descriptive_statistics.ipynb` |
| 02 | `02_probability_analysis.ipynb` | How do observed pressure probabilities compare with the assumed baseline? | Part C | Planned |
| 03 | `03_monte_carlo_simulation.ipynb` | Do simulated results agree with analytical and empirical probabilities? | Bonus | Planned |
| 04 | `04_bayesian_estimation.ipynb` | How uncertain is the unknown mean pressure? | Part D, implemented extension | Optional implementation |
| 05 | `05_engineering_interpretation.ipynb` | What do the results imply for infrastructure operations? | Part E; Part D conceptual answers; synthesis | Planned |

The core path for a minimum complete study is **01 → 02 → 03 → 05**. Notebook 04 is an optional implementation of Bayesian estimation; the conceptual questions in Part D must still be answered in notebook 05 if notebook 04 is not developed.

Do **not** create a separate `00_data_audit.ipynb` by default. Data validation, cleaning decisions, and diagnostic interpretation belong in the opening sections of notebook 01. A standalone audit notebook is justified only if auditing becomes a substantial independent deliverable.

### Optional Advanced Extensions

| # | Notebook | Focus | Prerequisite |
| --- | --- | --- | --- |
| 06 | `06_anomaly_detection.ipynb` | Statistical and/or ML detection of abnormal readings, evaluated against labels | EDA and baseline rules |
| 07 | `07_time_series_modeling.ipynb` | Autocorrelation, temporal structure, drift, and regime/change-point analysis | EDA |
| 08 | `08_reliability_risk_modeling.ipynb` | Scenario-based infrastructure risk and reliability, subject to available assumptions | Core engineering interpretation |
| 99 | `99_scratch_*.ipynb` | Temporary experiments, not committed or depended upon | None |

These extensions are **not required** by the original problem statement. Add them when their analytical questions are ready to be investigated. Do not use `anomaly_flag` as a predictive feature when evaluating anomaly detection against that same label.

## 01 — Exploratory Data Analysis

**Notebook:** `01_exploratory_data_analysis.ipynb` (existing file: `01_descriptive_statistics.ipynb`)

**Question:** What does the dataset contain, which observations are trustworthy for each calculation, and how does observed pressure behavior compare with `N(72, 4²)`?

**Scope:**

1. **Introduction and objectives:** State the engineering scenario, dataset, baseline assumptions, and Parts A/B deliverables.
2. **Imports and configuration:** Import the required libraries and project functions; establish paths and plotting conventions.
3. **Data loading and initial inspection:** Inspect shape, columns, types, timestamp coverage, representative records, and memory usage.
4. **Data quality assessment:** Examine missing values by sensor state, duplicate rows and timestamps (including conflicting duplicates), hourly continuity, categorical counts, invalid ranges, frozen readings, and implausible telemetry.
5. **Cleaning and preprocessing decisions:** Record each rule, rationale, affected record counts, and whether analysis uses raw, cleaned, or alternative filtered populations. Preserve the original dataset.
6. **Descriptive statistics (Part A):** Compute sample mean, sample variance, and sample standard deviation; report the sample size and inclusion/exclusion rules. Compare with 72 psi and 4 psi, including practical significance.
7. **Distribution visualization:** Create and interpret histograms, box plots, and, where useful, Q-Q plots; compare the observed distribution against the assumed normal baseline.
8. **Time-series exploration:** Plot pressure over time, examine rolling behavior and excursion periods, and investigate sensor state, pump state, and flow context.
9. **Z-scores and outlier analysis (Part B):** Compute baseline z-scores, count `|z| > 2` and `|z| > 3`, evaluate 81 psi, and investigate clustering and alignment with sensor status, pump status, and `anomaly_flag`.
10. **Preliminary engineering interpretation:** Summarize findings, limitations, data quality concerns, and the recommended analytical population for the next notebook.
11. **Outputs and handoff:** Document reusable preprocessing rules, relevant figures, and any processed dataset or summary artifact needed downstream.

**Important:** Missing pressures during `OFFLINE` should not automatically be interpolated. Similarly, a `DRIFT` or `FROZEN` state may indicate sensor unreliability rather than a true hydraulic event. Clearly distinguish sensor artifacts from possible operating abnormalities.

**Completion criteria:** Data quality decisions are documented; Parts A and B are answered; figures and statistics are interpreted; the notebook runs from a clean kernel; reusable functions have appropriate tests.

**Related document:** `01_descriptive_statistics_strategy.md`. Its existing ten-step outline remains the detailed foundation; the notebook management guide does not replace it.

## 02 — Probability Analysis

**Notebook:** `02_probability_analysis.ipynb`

**Question:** Assuming the original normal distribution is correct, how likely are high- and low-pressure events, and how do these predictions compare with observed telemetry?

**Scope:**

1. State the reference model `X ~ N(72, 4²)` and threshold definitions.
2. Compute theoretical `P(X > 80 psi)` and `P(X < 65 psi)` with SciPy; optionally cross-check using z-scores or z-tables.
3. Compute empirical exceedance frequencies for explicitly defined analytical populations.
4. Compare theoretical and empirical probabilities, including absolute differences and relative differences when meaningful.
5. Discuss whether departures could reflect a changed distribution, operating regimes, temporal clustering, sensor artifacts, or data-processing choices.
6. If useful, evaluate simple threshold/z-score rules against `anomaly_flag` as an optional baseline for a future anomaly-detection extension. This is **not** required to complete Part C.
7. Document statistical limitations, including autocorrelation and the difference between observed frequency and an assumed independent-observation probability model.

**Outputs:** Probability comparison table, documented assumptions, optional plots, and written conclusions about baseline consistency.

**Completion criteria:** Both theoretical probabilities and empirical comparisons are reported and explained using consistent denominators and clearly identified data populations.

## 03 — Monte Carlo Simulation

**Notebook:** `03_monte_carlo_simulation.ipynb`

**Question:** Does simulation reproduce analytical probabilities, and how does either compare with observed pressure behavior?

**Scope:**

1. State the assumed sampling distribution, parameters, number of draws (`100,000`), and fixed random seed.
2. Generate simulated pressure observations from the original normal baseline.
3. Estimate expected pressure and `P(X > 80 psi)`; optionally estimate `P(X < 65 psi)` for consistency with Part C.
4. Present suitable uncertainty intervals, explicitly identifying whether each is a Monte Carlo confidence interval for an estimated quantity or an interval describing simulated pressure values.
5. Plot the simulated distribution with the theoretical density and relevant thresholds.
6. Check convergence or Monte Carlo sampling variability as the number of draws increases.
7. Compare **analytical vs. simulated vs. observed** probabilities.
8. Explain the difference between Monte Carlo sampling error, uncertainty in model parameters, and potential structural mismatch between the normal baseline and real telemetry.
9. Optionally simulate an alternative scenario using parameters estimated from an explicitly defined observed population.

**Outputs:** Reproducible simulation, probability comparison, convergence plot, and written discussion of uncertainty.

**Completion criteria:** The 100,000-draw simulation is reproducible, its results are checked against analytical expectations, and differences from empirical telemetry are interpreted.

## 04 — Bayesian Estimation (Optional Implementation)

**Notebook:** `04_bayesian_estimation.ipynb`

**Question:** If the true mean pressure is uncertain, what can observed data tell us about its plausible values?

Part D requires conceptual reasoning; it does **not** require an implemented Bayesian or MCMC model. Build this notebook when ready to study posterior estimation in practice.

**Scope:**

1. Define the unknown parameter and an explicit prior, with engineering justification.
2. Define a likelihood and explain which assumptions are questionable for hourly telemetry (especially independence, stable mean, and measurement reliability).
3. Use a conjugate posterior where appropriate, or implement an MCMC approach if that adds learning value.
4. Report posterior summaries and credible intervals, and distinguish them from frequentist confidence intervals.
5. If using MCMC, inspect appropriate convergence and sampling diagnostics.
6. Test sensitivity to prior assumptions, preprocessing choices, and sensor-state filtering.
7. Explain why posterior uncertainty may be understated if autocorrelation or nonstationarity is ignored.

**Outputs:** Documented posterior analysis, visualizations, sensitivity discussion, and limitations.

**Completion criteria:** The method and its assumptions are explicit; posterior results are reproducible and interpreted without overstating certainty.

## 05 — Engineering Interpretation and Synthesis

**Notebook:** `05_engineering_interpretation.ipynb`

**Question:** Does the observed system remain consistent with its assumed pressure behavior, and what operational conclusions are justified?

**Scope:**

1. Summarize the analytical population, preprocessing decisions, and key results from prior notebooks.
2. Examine excursions above 80 psi and below 65 psi, including frequency, duration, consecutive-event runs, and timing.
3. Consider pump state, flow conditions, sensor reliability, and uncertainty in whether recorded events represent true hydraulic conditions.
4. Discuss which type of excursion may be more consequential **under the stated hypothetical risk assumptions**. Do not assert that one threshold is universally more dangerous without system-specific evidence.
5. Answer the Part D conceptual questions if notebook 04 was not developed: Monte Carlo usefulness, posterior sampling, and the benefits/limitations of Bayesian estimation.
6. Explain whether the original `N(72, 4²)` model remains a defensible description of the observations, including relevant qualifications.
7. Identify additional information needed for real engineering decisions: sensor calibration, pressure transients, system configuration, pipe ratings, demand/flow conditions, pump controls, and event corroboration.
8. State limitations, recommended follow-up investigations, and the difference between an educational synthetic-data conclusion and production-level decision support.
9. Provide a concise methods note covering cleaning, probability assumptions, uncertainty, and the most defensible analytical variant.
10. Present selected figures and tables suitable for a written report or future Power BI dashboard.

**Outputs:** Executive summary, engineering findings, methods note, limitations, and defensible recommendations. Reuse results from earlier notebooks rather than rebuilding their analyses unnecessarily.

**Completion criteria:** Part E and the Part D conceptual questions are answered; conclusions are traceable to evidence; limitations and next steps are explicit.

## Standard Notebook Sections

Use the following as a consistent template, adapting the emphasis to the notebook's purpose:

1. **Title, objective, and engineering question**
2. **Data sources, analytical population, and assumptions**
3. **Imports and reproducibility setup**
4. **Data loading or documented input artifacts**
5. **Relevant validation and preprocessing checks**
6. **Analysis, calculations, and figures**
7. **Interpretation immediately following major findings**
8. **Limitations, conclusions, and next steps**

A later notebook need not repeat the entire initial data audit, but it must verify that its input data and preprocessing version match its assumptions. Each notebook should be runnable independently from documented files and functions, not from variables left in another notebook's kernel.

## Cell-Level Practices

- Start each major section with a Markdown heading and a short statement of purpose.
- Keep code cells focused on one analytical step or a tightly related group of steps.
- Use descriptive variable names and deliberate, manageable displays rather than unexplained DataFrame dumps.
- Place interpretation immediately after important figures and tables.
- Distinguish **observations**, **model assumptions**, and **engineering judgment**.
- Record denominators, units, thresholds, filtering rules, and sample sizes.
- Avoid hidden state, out-of-order dependencies, and unexplained manual edits to intermediate data.
- Use `anomaly_flag` as reference labels for evaluation, not as proof that a particular statistical method is valid.

## Recommended Development Workflow

1. Define the notebook's analytical question and expected deliverable.
2. Identify the relevant data population and quality constraints.
3. Prototype a clear calculation or plot in the notebook.
4. Decide whether the logic is notebook-specific or reusable.
5. Move stable, reusable logic into the appropriate `src/suspicious_sensor/` module.
6. Add focused pytest unit tests, including edge cases.
7. Import and call tested functions from the notebook.
8. Explain numerical results and engineering implications in Markdown.
9. Restart the kernel and run all cells in order.
10. Check outputs, assumptions, data versions, and notebook diffs before committing.

## Data Handling and Analytical Populations

- Preserve `data/raw/` unchanged.
- Save derived datasets to `data/processed/` only when needed; document their creation and source.
- Clearly identify whether results use raw data, cleaned data, or a filtered subset.
- Maintain a **cleaning decision log** with reasons and affected record counts.
- Treat missing `pressure_psi` values, duplicate timestamps, sensor status, and telemetry artifacts as analytical decisions rather than silent preprocessing steps.
- Consider comparing **all valid pressure observations** with a **normal-sensor-state subset**. These represent different questions; neither is automatically the complete engineering truth.
- Distinguish an abnormal physical condition from an unreliable instrument reading.
- For time-series uncertainty, assess dependence and operating regimes before interpreting conventional independent-sample confidence intervals.
- If multiple populations or cleaning variants are evaluated, identify which is most defensible for each conclusion and why.

## Testing and Validation

**Unit tests:** Test reusable functions in `src/` using small synthetic DataFrames with targeted edge cases. Use the full project dataset sparingly for integration checks.

**Notebook checks:** Verify that imports resolve in the configured environment, all cells execute sequentially after a kernel restart, data paths are portable, and displayed outputs match current code and assumptions.

**Statistical checks:** Verify use of sample variance/standard deviation when requested, consistent treatment of missing values and duplicate records, correct denominators for empirical frequencies, and clear separation of reference-baseline and empirical parameter estimates.

**Simulation checks:** Fix seeds where appropriate, record parameters and sample size, compare simulated quantities with known analytical expectations, and distinguish numerical sampling variability from model uncertainty.

## Reproducibility and Version Control

- Use `pyproject.toml` and `uv.lock` for dependency management.
- Avoid machine-specific absolute paths and secrets.
- Keep generated data and large notebook outputs out of version control unless they serve a documented purpose.
- Review notebook diffs for accidental output changes before committing.
- Store essential results in reproducible files or recreate them through shared modules; do not depend on executing previous notebooks in the same kernel.
- Export notebooks to PDF when required by the project checklist, after validating their outputs.

## Notebook Completion Checklist

- [ ] Engineering question and scope stated
- [ ] Input data, analytical population, and assumptions documented
- [ ] Imports and loading work from a clean kernel
- [ ] Relevant diagnostics and cleaning decisions documented
- [ ] Statistical methods and sample sizes are appropriate and explicit
- [ ] Tables and figures have labels, units, and interpretation
- [ ] Findings distinguish sensor artifacts from potential system behavior
- [ ] Engineering implications and limitations are documented
- [ ] Reusable logic is extracted and tested where appropriate
- [ ] All cells run from top to bottom without errors
- [ ] Outputs and next-stage handoff are reproducible
- [ ] Notebook is reviewed and exported if required

## Project Sequence and Scope Control

**Phase 1: Required statistical investigation**

- Complete notebook 01 (EDA, Part A, Part B).
- Complete notebook 02 (Part C).
- Complete notebook 03 (Monte Carlo bonus, included in the planned project scope).
- Complete notebook 05 (Part D conceptual reasoning, Part E, and synthesis).

**Phase 2: Optional advanced work**

- Implement notebook 04 (Bayesian estimation and optional MCMC).
- Add notebooks 06–08 only when anomaly detection, time-series modeling, or reliability risk becomes a distinct project objective.

The numbering reserves a stable place for the optional Bayesian notebook; notebook 05 does not depend on notebook 04 existing.

## Relationship to Other Project Documents

- `01_problem_statement.md`: authoritative analytical questions and deliverables.
- `00_strategy_overview.md`: high-level software-component responsibilities.
- `01_descriptive_statistics_strategy.md`: detailed workflow for the first notebook.
- `00_mvp_checklist.md`: implementation and deliverable tracking, if present in the repository.
- `01_structure.md`: repository layout; update it when actual notebook names or folders change.

This document governs notebook working practices and the recommended notebook roadmap. It does not replace the problem statement, the detailed EDA strategy, or the implementation checklist.
