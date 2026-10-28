# Standard Python Docstring Template

The most common professional Python docstring format today is based on:
- Google Style
- NumPy Style
- reStructuredText (RST)

Recommended Style:
# Google Style Docstrings
- clean,
- readable,
- IDE-friendly,
- beginner-to-advanced friendly,
- and widely used in production Python codebases.

Because some docstring formats appear to have been designed specifically to emotionally punish developers.

---

# Standard Google Style Template

```python
def function_name(parameter_1: type, parameter_2: type) -> return_type:
    """
    Short summary of what the function does.

    Optional longer explanation providing additional detail
    about the purpose, behavior, assumptions, or workflow.

    Args:
        parameter_1 (type):
            Description of parameter_1.

        parameter_2 (type):
            Description of parameter_2.

    Returns:
        return_type:
            Description of returned value.

    Raises:
        ExceptionType:
            Description of when this exception occurs.

    Notes:
        Optional implementation details, assumptions,
        warnings, or engineering considerations.

    Example:
        >>> function_name(1, 2)
        3
    """
```

---

# Example — Infrastructure Dataset Validation

```python
def validate_pressure_ranges(
    df: pd.DataFrame,
    min_pressure: float = 0.0,
    max_pressure: float = 200.0
) -> pd.DataFrame:
    """
    Validate pressure sensor readings against expected operational limits.

    This function identifies rows containing pressure values
    outside the expected infrastructure operating range.

    Args:
        df (pd.DataFrame):
            DataFrame containing pressure sensor readings.

        min_pressure (float):
            Minimum allowable pressure threshold in psi.

        max_pressure (float):
            Maximum allowable pressure threshold in psi.

    Returns:
        pd.DataFrame:
            Subset of rows containing invalid pressure values.

    Raises:
        KeyError:
            Raised if the required pressure column does not exist.

    Notes:
        This validation is intended for preliminary data quality
        inspection and should not replace engineering review.

    Example:
        >>> invalid_rows = validate_pressure_ranges(df)
    """
```

---

# Minimal Professional Version

Sometimes simpler is better.

```python
def calculate_mean(values: list[float]) -> float:
    """
    Calculate the arithmetic mean of a numeric list.

    Args:
        values (list[float]):
            List of numeric values.

    Returns:
        float:
            Arithmetic mean of the input values.
    """
```

---

# Sections You Will Commonly Use

| Section | Purpose |
|---|---|
| `Args:` | Input parameters |
| `Returns:` | Return value |
| `Raises:` | Exceptions |
| `Notes:` | Engineering assumptions/details |
| `Example:` | Usage examples |

---

# Sections You Usually Do NOT Need

Avoid overengineering docstrings for tiny functions.

You do NOT need this:

```python
def add(a, b):
    """
    Adds two numbers together.
    """
```

That provides almost no value.

Docstrings should explain:
- purpose,
- assumptions,
- behavior,
- constraints,
- engineering intent.

Not narrate obvious syntax like a nature documentary.

---

# My Recommendation for Your Projects

For your infrastructure analytics work:

Use:
- type hints,
- Google-style docstrings,
- explicit assumptions,
- engineering notes when appropriate.

That combination looks:
- professional,
- maintainable,
- backend-oriented,
- and engineering-grade.

Especially for:
- utilities,
- probabilistic systems,
- reliability workflows,
- infrastructure analytics pipelines.

Because eventually someone will revisit your code six months later and ask:
> “Why was the pressure threshold set to 80 psi?”

And future-you deserves documentation instead of forensic archaeology.