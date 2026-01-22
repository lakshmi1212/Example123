# Math Operations Example

This repository provides basic math operations (addition and subtraction) implemented in Python, along with comprehensive pytest-based test coverage.

## Folder Structure

- `src/`: Contains the production code (`math_operations.py`).
- `tests/`: Contains test files for each operation (`test_add.py`, `test_subtract.py`).
- `default/`: Contains workflow metadata (`math.json`), requirements, and documentation.

## Usage

1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Run all tests:
   ```bash
   python -m pytest tests/ -v --tb=short
   ```

## CI Workflow

This repository is set up for GitHub Actions CI. Workflow metadata can be found in `default/math.json`. The workflow runs tests on every push and pull request to the `main` branch.
