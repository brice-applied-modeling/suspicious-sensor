# Comparing Objects in Pandas

One of the more common sources of confusion when writing tests with Pandas is knowing when to use the `==` operator versus the `.equals()` method.

The correct choice depends on the type of object being compared.

---

## Use `==` for Native Python Types

Python's built-in data structures should be compared using the equality operator.

Examples include:

- `int`
- `float`
- `str`
- `bool`
- `list`
- `tuple`
- `dict`
- `set`

### Example

```python
actual = {"A": 10, "B": 20}
expected = {"A": 10, "B": 20}

assert actual == expected
```

Python automatically compares the contents of the dictionaries.

---

## Use `.equals()` for Pandas Objects

Pandas provides the `.equals()` method for comparing:

- `pd.Series`
- `pd.DataFrame`

Unlike Python objects, Pandas objects contain additional metadata such as:

- Index values
- Column labels
- Data types
- Missing values

The `.equals()` method performs an element-by-element comparison while also ensuring the structure matches.

### Series Example

```python
actual = df.dtypes
expected = other_df.dtypes

assert actual.equals(expected)
```

### DataFrame Example

```python
assert actual_df.equals(expected_df)
```

---

## Why Not Use `==` with Pandas?

Suppose we compare two Series:

```python
actual = df.dtypes
expected = other_df.dtypes

assert actual == expected
```

This does **not** produce a single Boolean value.

Instead, Pandas returns another Series.

Example:

```text
temperature     True
pressure        True
flow_rate      False
dtype: bool
```

Now Python attempts to evaluate whether this Series is "True" or "False."

Since multiple values exist, Pandas raises:

```text
ValueError:
The truth value of a Series is ambiguous.
```

Pandas doesn't know whether you mean:

- Are **all** values True?
- Is **any** value True?
- Something else?

Using `.equals()` avoids this ambiguity.

---

## Example from `dataset_diagnostics()`

### Data Types

`df.dtypes` returns a **Pandas Series**.

```python
actual_dtypes = result["data_types"]
expected_dtypes = df.dtypes

assert actual_dtypes.equals(expected_dtypes)
```

This is the correct approach.

---

### Unique Values

Suppose the function returns:

```python
{
    "temperature": 25,
    "pressure": 41,
    "status": 2
}
```

This is a standard Python dictionary.

The expected result is generated with:

```python
expected_unique = df.nunique().to_dict()
```

Notice the call to `.to_dict()`.

This converts the Pandas Series into a Python dictionary.

The comparison should therefore be:

```python
assert actual_unique == expected_unique
```

Using `.equals()` would fail because dictionaries do not have an `.equals()` method.

---

## Summary

| Object Type | Comparison Method |
|-------------|-------------------|
| `int` | `==` |
| `float` | `==` |
| `str` | `==` |
| `bool` | `==` |
| `list` | `==` |
| `tuple` | `==` |
| `dict` | `==` |
| `set` | `==` |
| `pd.Series` | `.equals()` |
| `pd.DataFrame` | `.equals()` |

---

## Rule of Thumb

If you're working with standard Python objects, use the `==` operator.

If you're comparing Pandas `Series` or `DataFrame` objects, use the `.equals()` method.

Understanding the distinction makes writing unit tests with Pandas much more predictable and helps avoid one of the most common errors encountered by new Pandas users.
