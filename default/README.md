# Example123 Math Operations

This repository provides basic math operations (addition and subtraction) implemented in Python.

## Usage

Import the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
```

## Testing

Tests are located in the `tests/` folder. Run all tests using:

```sh
python -m pytest tests/ -v --tb=short
```

## CI Workflow

Continuous integration is handled via GitHub Actions in `.github/workflows/ci.yml`.

## Requirements

See `default/requirements.txt` for dependencies.
