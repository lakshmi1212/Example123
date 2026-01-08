# Math Operations

This repository provides simple math operations (addition and subtraction) implemented in Python.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/lakshmi1212/Example123.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Example123
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run tests:
   ```bash
   pytest
   ```

## CI Workflow

This repository is integrated with a CI pipeline that runs tests on every push or pull request to the `main` branch. The workflow is defined in `.github/workflows/ci.yml`.

## Files

- `src/math_operations.py`: Contains the implementation of addition and subtraction functions.
- `tests/test_add.py`: Contains test cases for the addition function.
- `tests/test_subtract.py`: Contains test cases for the subtraction function.
- `requirements.txt`: Lists dependencies.
- `math.json`: Metadata for CI workflow generation.
