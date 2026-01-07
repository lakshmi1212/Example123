# Math Operations

This repository contains Python functions for basic math operations (addition and subtraction) and corresponding test cases using pytest.

## Files

- **src/math_operations.py**: Contains the implementation of addition and subtraction functions.
- **tests/test_add.py**: Contains test cases for the addition function.
- **tests/test_subtract.py**: Contains test cases for the subtraction function.

## How to Run Tests

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run tests using pytest:
   ```
   pytest tests/
   ```

## CI Workflow

This repository is configured for CI workflows using GitHub Actions. The workflow runs tests automatically on every push or pull request to the `main` branch.