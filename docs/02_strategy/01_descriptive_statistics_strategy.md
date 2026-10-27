# Descriptive Statistics Notebook Strategy
This document defines the steps and strategy to be used and implemented to complete the descriptive statistics analysis.

## Libraries Required
- Numpy
- Pandas
- Matplotlib
- Seaborn

## Organization
- The notebook analysis will be performed in the `notebooks/` folder
- The functions used to perform the analysis will be in the `src/utils/` folder.

### Utility Functions
- [x] Load Data
- [ ] Dataset Inspection
  - [x] Shape
  - [ ] Data Type
  - [ ] Any missing data
  - [ ] Duplications
  - [ ] Memory usage
    - [ ] how much RAM the dataframe consumes
    - [ ] `df.memory_usage(deep=True)`
    - [ ] `df.info(memory_usage='deep')`
  - [ ] Unique values (select columns)
  - [ ] Dataset validation checks
    - [ ] Validate that dataset columns contain expected structures, values, and datatypes.
    - [ ] are the columns present?
    - [ ] are they spelled correctly?
    - [ ] are the data types correct (ie: datestamp, float, etc.)
  - [ ] **Validate Value Ranges**
    - [ ] Example:
      - [ ] pressure should not be:
      - [ ] negative
      - [ ] 9000 psi
      - [ ] NaN everywhere
  - [ ] **Timestamp Validation**
    - [ ] Check:
      - [ ] timestamps parse correctly,
      - [ ] timestamps are ordered,
      - [ ] timestamps are unique,
      - [ ] timestamps are not missing.
- [ ] Data Cleaning
  - [ ] missing value handling
  - [ ] datatype conversions
  - [ ] timestamp parsing
  - [ ] duplicate removal
- [ ] Descriptive Statistics
  - [ ] mean
  - [ ] variance
  - [ ] standard deviation
- [ ] Visualizations
  - [ ] histogram
  - [ ] box plots
  - [ ] distribution plots
  - [ ] time series plots
- [ ] Time Series Exploration
  - [ ] pressure over time
  - [ ] rolling mean
  - [ ] rolling standard deviation
  - [ ] Trend inspection
  - [ ] excursion periods

## Notebook Structure
1. Import Libraries
2. Load Dataset
3. Dataset Inspection
4. Data Cleaning / Validation
5. Descriptive Statistics
6. Distribution Visualization
7. Time-Series Visualization
8. Z-Score Analysis
9. Outlier Investigation
10. Initial Engineering Interpretation

## Special Considerations
This section discusses what should not be included in utils and what the utils should include.

### Utility Functions should NOT be included
- df.shape
- df.describe()
- simple one-line operations.

### Utility Functions SHOULD include
- reusable logic
- repeated workflows
- validation pipelines
- transformations
- plotting logic
- Utility functions should support future logging integration

## Reproducibility
- fixed random seeds where applicable
- deterministic simulations where practical
- documented assumptions
- reproducible plots and outputs

## Future Expansion
- Monte Carlo simulation
- Bayesian estimation
- anomaly detection
- predictive modeling
- infrastructure reliability analysis
