# Project Structure

## Repository Tree

```plaintext
suspicious_sensor/
├── .gitignore                             # Comprehensive Python/data/IDE ignore rules
├── .python-version                        # Python 3.12 version pin
├── pyproject.toml                         # Project metadata and dependencies
├── uv.lock                                # UV lockfile for reproducible environments
├── README.md                              # Project overview and learning objectives
│
├── data/
│   ├── raw/
│   │   └── pressure_sensor_readings.csv   # ~4,340 hourly sensor readings (2026-01-01 onward)
│   └── processed/                         # Derived datasets (gitignored; empty)
│
├── docs/
│   ├── 00_overveiw/
│   │   ├── 01_problem_statement.md        # Problem scenario and five-part analysis framework
│   │   ├── 02_data.md                     # Dataset description and column definitions
│   │   └── 03_docstring_template.md       # Google-style docstring standards
│   │
│   ├── 01_architecture/
│   │   └── 01_structure.md                # This file — directory layout and organization rationale
│   │
│   ├── 02_strategy/
│   │   └── 01_descriptive_statistics_strategy.md  # 10-step analysis workflow and utility design
│   │
│   ├── 03_dashboard/
│   │   └── 00_power_bi_dashboard_plan.md  # Power BI dashboard specification
│   │
│   └── 04_checklists/
│       └── 00_mvp_checklist.md            # MVP feature tracking checklist
│
├── notebooks/
│   ├── 01_descriptive_statistics.ipynb    # Exploratory data analysis notebook
│   └── 01_descriptive_statistics.pdf      # PDF export of notebook
│
├── src/
│   └── suspicious_sensor/
│       ├── __init__.py                    # Package marker
│       ├── main.py                        # CLI entry point stub
│       │
│       ├── io/
│       │   ├── __init__.py                # Package marker
│       │   └── loader.py                  # load_data(filename) — loads CSV from data/raw/
│       │
│       ├── diagnostics/
│       │   ├── __init__.py                # Package marker
│       │   ├── diagnostics.py             # dataset_diagnostics(df) — shape, dtypes, memory, unique values
│       │   ├── cleaning.py 
│       │   └── validation.py              # dataset_validation(df) — stub
│       │
│       ├── preprocessing/
│       │   └── __init__.py                # Package marker (planned)
│       │
│       ├── statistics/
│       │   ├── __init__.py                # Package marker (planned)
│       │   ├── descriptive.py
│       │   ├── probability.py
│       │   └── z_scores.py
│       │
│       ├── models/
│       │   └── __init__.py                # Package marker (planned)
│       │
│       ├── simulation/
│       │   ├── __init__.py                # Package marker (planned)
│       │   └── monte_carlo.py
│       │
│       └── visualization/
│           ├── __init__.py                # Package marker (planned)
│           ├── distributions.py
│           └── time_series.py
│
└── tests/
    ├── __init__.py                        # Test package marker
    └── unit_tests/
        ├── __init__.py                    # Test sub-package marker
        ├── test_load_data.py              # Tests for io.loader.load_data()
        └── test_dataset_diagnostics.py    # Tests for diagnostics.dataset_diagnostics()
```

## Directory Rationale

| Directory                               | Purpose |
|-----------------------------------------|---------|
| `data/raw/`                             | Immutable source data; never modified in place |
| `data/processed/`                       | Derived or cleaned datasets (gitignored) |
| `docs/`                                 | Human-readable documentation organized by topic |
| `notebooks/`                            | Exploratory analysis and visualization (not production code) |
| `src/suspicious_sensor/io/`             | Data loading — reads CSV files from `data/raw/` |
| `src/suspicious_sensor/diagnostics/`    | Dataset inspection — shape, dtypes, memory, unique values, validation |
| `src/suspicious_sensor/preprocessing/` | Data cleaning and transformation (planned) |
| `src/suspicious_sensor/statistics/`    | Statistical calculations — z-scores, distributions (planned) |
| `src/suspicious_sensor/models/`        | Estimation and modeling (planned) |
| `src/suspicious_sensor/simulation/`    | Monte Carlo / MCMC simulations (planned) |
| `src/suspicious_sensor/visualization/` | Plotting and visualization utilities (planned) |
| `tests/unit_tests/`                     | Unit tests for `src/` modules |

## Key Files

| File                                                          | Role |
|---------------------------------------------------------------|------|
| `pyproject.toml`                                              | Declares dependencies (numpy, pandas, matplotlib, seaborn, pytest, ipykernel, pyright) and Python ≥3.12 |
| `uv.lock`                                                     | Pins exact transitive dependency versions for reproducibility |
| `src/suspicious_sensor/io/loader.py`                          | `load_data(filename)` — resolves path relative to `data/raw/`, validates input, returns DataFrame |
| `src/suspicious_sensor/diagnostics/diagnostics.py`            | `dataset_diagnostics(df)` — returns dict with `shape`, `data_types`, `memory_usage`, `unique_values` |
| `src/suspicious_sensor/diagnostics/validation.py`             | `dataset_validation(df)` — stub; intended to validate structure, types, value ranges, timestamps |
| `data/raw/pressure_sensor_readings.csv`                       | ~4,340 rows: `timestamp`, `pressure_psi`, `flow_gpm`, `sensor_status`, `pump_status`, `anomaly_flag` |
| `tests/unit_tests/test_load_data.py`                          | 3 tests: return type, TypeError on bad input, FileNotFoundError on missing file |
| `tests/unit_tests/test_dataset_diagnostics.py`                | 8 tests: 2 implemented (return type, expected keys), 6 stubs pending implementation |

## Implemented vs. Planned Modules

| Module          | Status      | Key Exports |
|-----------------|-------------|-------------|
| `io`            | Implemented | `load_data(filename)` |
| `diagnostics`   | Partial     | `dataset_diagnostics(df)` implemented; `dataset_validation(df)` stub |
| `preprocessing` | Planned     | — |
| `statistics`    | Planned     | — |
| `models`        | Planned     | — |
| `simulation`    | Planned     | — |
| `visualization` | Planned     | — |

## Conventions

- **Src layout**: all application code lives under `src/suspicious_sensor/` to enforce clean import boundaries and prevent accidental imports from the project root.
- **Domain modules**: functionality is split by concern (`io`, `diagnostics`, `statistics`, etc.) rather than by file type, so each module can be developed and tested independently.
- **Utilities first**: analysis logic is extracted from notebooks into `src/` modules to keep notebooks clean and enable unit testing.
- **Raw data is read-only**: processed or derived datasets live under `data/processed/` (gitignored).
- **Numbered docs**: prefixes (`00_`, `01_`, `02_`, …) reflect the intended reading/execution order.
- **Test mirroring**: tests live under `tests/unit_tests/` and mirror the module under test (e.g., `test_load_data.py` tests `io/loader.py`).
