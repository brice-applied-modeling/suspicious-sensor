
# Suspicious Sensor Analysis
*A Probability, Statistics, and Monte Carlo Engineering Exercise*

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Status](https://img.shields.io/badge/status-active%20development-orange)
![Focus](https://img.shields.io/badge/focus-probability%20%7C%20statistics%20%7C%20simulation-informational)
![Simulation](https://img.shields.io/badge/simulation-Monte%20Carlo-darkgreen)
![Domain](https://img.shields.io/badge/domain-infrastructure%20analytics-critical)
![Math](https://img.shields.io/badge/math-statistics%20%26%20bayesian%20reasoning-purple)
![Data](https://img.shields.io/badge/data-synthetic%20sensor%20dataset-lightgrey)
![Difficulty](https://img.shields.io/badge/level-intermediate-red)

## Project Overview

Suspicious Sensor Analysis is a Python-based infrastructure analytics project exploring the application of probability, statistics, Monte Carlo simulation, and Bayesian reasoning to pressure monitoring and operational uncertainty.

The project investigates how statistical methods can help engineers distinguish ordinary operating variability from potentially significant pressure anomalies.

Primary areas of investigation include:

- Descriptive statistics and exploratory data analysis
- Z-scores and statistical anomaly detection
- Probability distributions and threshold exceedances
- Monte Carlo simulation
- Bayesian reasoning about parameter uncertainty (optional implementation)
- Engineering interpretation of sensor observations

The long-term objective is to establish a reproducible analytical workflow that translates sensor measurements into defensible engineering observations and risk-informed decisions.

---

## Project Status and Versioning

**Current Version:** v0.1.0  
**Development Status:** Active Development  
**Target Initial Release:** v1.0.0

The project follows Semantic Versioning using the format:

`MAJOR.MINOR.PATCH`

| Component | Description |
|---|---|
| MAJOR | Significant changes to established functionality or compatibility |
| MINOR | New analytical capabilities or enhancements |
| PATCH | Bug fixes, corrections, and minor improvements |

### Development Versions

Versions below `1.0.0` represent development releases. Analytical methods, implementation details, and project structure may change as the project matures.

### Stable Release

Version `1.0.0` will represent completion of the initial project scope, including validated statistical analysis, Monte Carlo simulation, documented engineering interpretation, and reproducible results.

Future functionality may continue through subsequent minor and major releases without changing the completed status of the initial project.

---

## Engineering Scenario

A water utility installs a pressure sensor on a transmission main.

Engineers initially assume that operating pressure follows a normal distribution:

```text
Mean (μ) = 72 psi
Standard deviation (σ) = 4 psi
```

Operators subsequently observe indications of abnormal pressure instability.

A synthetic sensor dataset is used to investigate:

- Pressure variability
- Potential outliers
- Operational excursions
- Changes in operating conditions
- Statistical and engineering uncertainty

The objective is to determine whether observed behavior is consistent with expected operating conditions or warrants further engineering investigation.

Statistical anomalies are treated as indicators requiring interpretation, not automatic evidence of infrastructure failure.

---

## Dataset Overview

The synthetic dataset includes:

- Timestamped pressure observations
- Normal operational fluctuations
- Gradual pressure drift
- Low-pressure excursions
- High-pressure anomalies
- Potential outlier conditions

The dataset contains **4,340 synthetic telemetry observations** with six fields: `timestamp`, `pressure_psi`, `flow_gpm`, `sensor_status`, `pump_status`, and `anomaly_flag`. It includes normal, drifting, frozen, and offline sensor conditions, along with missing pressure readings and duplicate-record challenges.

The dataset is designed to represent realistic analytical challenges, including noisy observations and changing operating conditions. See [Dataset Documentation](docs/00_overview/02_data.md) for definitions and generation assumptions.

Because the dataset is synthetic, results demonstrate analytical methods rather than establish actual infrastructure performance or reliability.

---

## Learning and Analytical Objectives

The project is designed to develop and demonstrate competency in:

- Descriptive statistics
- Sample variance and standard deviation
- Z-score analysis
- Probability distributions
- Statistical inference
- Monte Carlo simulation
- Confidence interval estimation
- Bayesian reasoning
- Infrastructure risk interpretation
- Engineering uncertainty

An additional objective is to develop a documented, reproducible Python workflow that can be independently executed and reviewed.

---

## Analytical Methods

### 1. Descriptive Statistics

Analyze the statistical properties of the pressure observations.

Methods include:

- Mean and median
- Variance and standard deviation
- Minimum and maximum values
- Quantiles and percentiles
- Distribution visualization
- Outlier identification
- Temporal variability

### 2. Probability Analysis

Evaluate pressure behavior relative to assumed or estimated probability distributions.

Topics include:

- Normal distribution assumptions
- Z-score calculations
- Tail probabilities
- Threshold exceedance probabilities
- Distribution diagnostics
- Sensitivity to statistical assumptions

### 3. Monte Carlo Simulation

Use repeated random sampling to explore uncertainty in pressure behavior and operational outcomes.

Methods include:

- Random sampling
- Synthetic pressure simulation
- Probability estimation
- Confidence intervals
- Distribution visualization
- Sensitivity analysis

Simulation results must distinguish between variability in pressure observations and uncertainty in estimated model parameters.

### 4. Bayesian Reasoning and Optional MCMC Methods

Explore probabilistic inference and parameter uncertainty.

Potential methods include:

- Prior distributions
- Likelihood functions
- Posterior estimation
- Bayesian credible intervals
- Markov Chain Monte Carlo sampling
- Posterior predictive analysis

Advanced Bayesian and MCMC methods are considered future enhancements unless explicitly included in the initial release scope.

---

## Project Architecture

The repository layout, module responsibilities, and directory conventions are maintained in [Project Structure](docs/01_architecture/01_structure.md). That document is the source of truth for the project tree; the README intentionally does not duplicate it.

---

## Analytical Workflow

The intended workflow is:

1. Load and validate the synthetic sensor dataset.
2. Perform exploratory data analysis.
3. Calculate descriptive statistics.
4. Evaluate distribution assumptions.
5. Identify potential anomalies and pressure excursions.
6. Estimate threshold exceedance probabilities.
7. Develop and execute Monte Carlo simulations.
8. Quantify simulation uncertainty and sensitivity.
9. Interpret results within an infrastructure engineering context.
10. Document findings, assumptions, limitations, and recommendations.

Each analytical stage should produce reproducible outputs suitable for technical review.

---

## Development Roadmap

The project is organized into seven phases. The [MVP Checklist](docs/02_strategy/00_mvp_checklist.md) tracks detailed implementation and testing tasks; notebook names below identify the intended analytical deliverables.

| Phase | Focus | Primary notebook |
|---|---|---|
| 1 | Data infrastructure, validation, and preprocessing | `notebooks/01_exploratory_data_analysis.ipynb` |
| 2 | Exploratory data analysis, descriptive statistics, and z-scores | `notebooks/01_exploratory_data_analysis.ipynb` |
| 3 | Probability analysis and threshold exceedances | `notebooks/02_probability_analysis.ipynb` |
| 4 | Monte Carlo simulation and uncertainty | `notebooks/03_monte_carlo_simulation.ipynb` |
| 5 | Bayesian reasoning; implementation optional | `notebooks/04_bayesian_estimation.ipynb` (optional) |
| 6 | Engineering interpretation | `notebooks/05_engineering_interpretation.ipynb` |
| 7 | Final validation, reproducibility, and release | All required notebooks |

Core functionality is implemented in reusable Python modules and verified with automated tests as it is developed. The notebooks present the analysis, figures, assumptions, and engineering interpretation.

**Current development:** Phase 1. Data loading, diagnostics, and portions of missing-data and duplicate analysis have been implemented. Dataset validation, preprocessing verification, and subsequent analytical phases remain in progress. The last reported test baseline was **14 passing tests**; this has not been independently rerun for this README update.

### Release Milestones

| Version | Target |
|---|---|
| `v0.1.0` | Project foundation and initial data utilities |
| `v0.2.0` | Validated exploratory analysis |
| `v0.3.0` | Probability and anomaly analysis |
| `v0.4.0` | Monte Carlo simulation |
| `v0.5.0` | Engineering interpretation |
| `v0.9.0` | Release candidate and reproducibility review |
| `v1.0.0` | Initial stable release |

These are planned milestones, not claims that the corresponding releases have been completed.

---

## Future Enhancements

Following the initial stable release, potential enhancements include:

- Bayesian parameter estimation
- Markov Chain Monte Carlo (MCMC)
- Time-series forecasting
- Advanced sensor anomaly detection
- Infrastructure reliability modeling
- Predictive maintenance analytics
- Hydraulic system simulation
- Risk scoring pipelines
- Interactive visualization or dashboards

These capabilities are not required for the initial stable release.

Future development should be evaluated based on its analytical value rather than the number of additional features.

---

## Python Libraries

Core analytical libraries may include:

```text
numpy
pandas
scipy
matplotlib
seaborn
```

Additional libraries for future development may include:

```text
pymc
arviz
statsmodels
jupyter
```

Actual project dependencies should be maintained in the project's dependency configuration.

---

## Example Analytical Questions

### Statistical Analysis

- Does the observed pressure distribution appear normally distributed?
- Are significant outliers present?
- Is the operating mean shifting over time?
- Does variability change across operating periods?

### Engineering Interpretation

- Are high-pressure excursions operationally significant?
- Could low-pressure excursions indicate service or operational risk?
- Is additional monitoring justified?
- Do observed conditions warrant further hydraulic investigation?

### Simulation and Uncertainty

- What is the estimated probability of pressure exceeding 80 psi?
- How frequently might low-pressure conditions occur?
- How sensitive are the results to changes in variance?
- How much uncertainty exists in the estimated probabilities?

---

## Testing and Reproducibility

The project will prioritize reproducibility and analytical validation.

Automated tests are developed alongside the corresponding modules. Testing should address:

- Input data validation
- Statistical calculation accuracy
- Probability estimation
- Simulation reproducibility
- Numerical edge cases
- Consistency between analytical outputs and documented findings

Monte Carlo simulations should use controlled random seeds when reproducible results are required.

Analytical conclusions should distinguish model assumptions, simulation estimates, and observed data characteristics.

---

## Release Management

Completed release milestones may be associated with Git version tags after review.

Example:

```bash
git tag -a v0.1.0 -m "Initial project foundation"
git push origin v0.1.0
```

Tags should only be created after the corresponding release milestone has been completed and reviewed.

Release notes should document:

- New functionality
- Analytical improvements
- Corrections and bug fixes
- Changes to assumptions or methodology
- Known limitations

A `CHANGELOG.md` file may be maintained to document release history.

---

## Repository Notes

Suspicious Sensor Analysis combines infrastructure engineering, statistics, simulation, and probabilistic reasoning.

The project is intended to demonstrate not only the implementation of analytical methods but also their interpretation within realistic engineering decision-making.

The primary objective is to develop a technically defensible and reproducible analytical workflow.

Engineering decisions require more than identifying unusual measurements. They require understanding what the measurements mean, how uncertain the conclusions are, and whether further investigation is justified.

---

## Project Lifecycle

The project will transition through the following stages:

**Active Development → Initial Stable Release → Maintenance & Enhancements**

Following the v1.0.0 release, the project may continue to receive corrections, analytical improvements, and additional capabilities.

The initial project will nevertheless be considered completed once its defined release requirements have been satisfied.
