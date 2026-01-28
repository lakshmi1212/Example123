# Math Operations Example

This repository provides basic math operations (addition and subtraction) with production-ready test automation and CI/CD integration.

## Structure
- `src/math_operations.py`: Business logic for add and subtract functions.
- `tests/test_add.py`, `tests/test_subtract.py`: Pytest test cases for math operations.
- `default/requirements.txt`: Python dependencies for testing.
- `default/math.json`: Metadata for CI workflow generation.

## Usage
```
from src.math_operations import add, subtract
print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

## Testing
Install dependencies and run tests:
```
pip install -r default/requirements.txt
pytest tests/ -v --tb=short
```

## CI/CD
Refer to `default/math.json` for workflow metadata. The CI pipeline runs all tests on push and pull requests targeting the `main` branch.
