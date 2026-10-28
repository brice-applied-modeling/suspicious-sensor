# Notebook Management Strategy

## Purpose

This guide establishes consistent practices for developing, organizing, validating, and maintaining Jupyter notebooks in the Suspicious Sensor project. Notebooks are reproducible analytical reports, not substitutes for reusable application modules.

## Roles and Boundaries

| Location | Responsibility |
| --- | --- |
| `notebooks/` | Exploratory analysis, presentation of results, plots, assumptions, and engineering interpretation |
| `src/suspicious_sensor/io/` | Reusable data loading |
| `src/suspicious_sensor/diagnostics/` | Diagnostics and validation |
| `src/suspicious_sensor/preprocessing/` | Cleaning and transformations |
| `src/suspicious_sensor/statistics/` | Reusable statistical calculations |
| `src/suspicious_sensor/simulation/` | Reusable simulation logic |
| `src/suspicious_sensor/visualization/` | Reusable plotting logic where warranted |
| `tests/unit_tests/` | Tests for application functions |

Simple, transparent one-line exploratory operations may remain in notebooks. Extract code when it is reused, requires substantial validation, or represents a stable analytical operation. Avoid creating utility functions solely to wrap basic pandas operations.

## Notebook Organization

Use descriptive, ordered filenames. The existing notebook is `01_descriptive_statistics.ipynb`. Additional notebooks should be created only when they represent distinct analytical questions, rather than splitting work arbitrarily. Potential later notebooks include probability analysis and Monte Carlo simulation; these are proposals, not committed deliverables.

For each notebook, include:

1. **Title and objective**: What engineering question is being answered?
2. **Dataset and assumptions**: Data source, baseline assumptions, and known limitations.
3. **Imports and setup**: Dependencies and reproducibility settings.
4. **Data loading**: Call the project loader rather than duplicating file-path logic.
5. **Inspection and validation**: Establish data quality before relying on results.
6. **Analysis**: Present calculations and plots in a logical sequence.
7. **Interpretation**: Explain what findings mean operationally, not just numerically.
8. **Limitations and next steps**: Identify unresolved issues and decisions.

The descriptive statistics notebook already has a ten-section plan in `01_descriptive_statistics_strategy.md`; follow that specific outline where applicable.

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
5. If reusable, move the logic to the appropriate `src/suspicious_sensor/` module.
6. Write focused unit tests for that module, including meaningful edge cases.
7. Import and call the tested function from the notebook.
8. Explain the result and its engineering significance in Markdown.
9. Restart the kernel and run all cells from top to bottom.
10. Review outputs, assumptions, and reproducibility before committing changes.

## Data Handling

- Keep `data/raw/` unchanged.
- Store derived datasets under `data/processed/` when necessary.
- Clearly label whether each result uses raw data, cleaned data, or both.
- Document cleaning criteria, especially missing pressures, duplicate timestamps, non-`NORMAL` sensor states, and telemetry artifacts.
- Do not use `anomaly_flag` as a substitute for independent anomaly reasoning; use it for subsequent validation or comparison.

## Testing and Validation

**Unit tests:** Test functions in `src/` with pytest. Prefer small synthetic DataFrames for focused cases; use the project dataset for a limited number of integration-style checks.

**Notebook checks:** Confirm imports work in the configured environment, cells execute sequentially after a kernel restart, outputs are consistent with stated assumptions, and no stale outputs contradict the current code.

**Simulation checks:** Fix random seeds where appropriate, record simulation settings and sample sizes, and distinguish Monte Carlo variability from uncertainty in model assumptions.

## Reproducibility and Version Control

- Use the project's `pyproject.toml` and `uv.lock` to maintain a reproducible environment.
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

- `00_strategy_overview.md`: high-level component responsibilities.
- `01_descriptive_statistics_strategy.md`: specific analytical sequence and scope.
- `00_mvp_checklist.md`: tracks implementation and deliverable completion.
- `01_structure.md`: documents repository layout.

This document governs notebook working practices; it does not replace the analytical strategy or project checklist.
