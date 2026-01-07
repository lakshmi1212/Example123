# Math Operations

This repository contains basic mathematical operations implemented in Python, along with their test cases.

## Files

- **src/math_operations.py**: Contains the `add` and `subtract` functions.
- **tests/test_add.py**: Test cases for the `add` function.
- **tests/test_subtract.py**: Test cases for the `subtract` function.
- **math.json**: Metadata file for CI/CD workflow generation.
- **requirements.txt**: Lists the dependencies for the project.

## Usage

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the test cases using `pytest`.

## CI/CD Workflow

The repository is configured to trigger workflows on push and pull requests to the `main` branch. The workflow includes running tests using `pytest`.