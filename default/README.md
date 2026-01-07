# Math Operations

This repository contains basic math operations implemented in Python, including addition and subtraction. It also includes test cases and a CI/CD pipeline configuration.

## Usage

The `math_operations.py` file in the `src` folder provides the following functions:

- `add(a, b)`: Adds two numbers.
- `subtract(a, b)`: Subtracts one number from another.

## Workflow

The CI/CD pipeline runs tests automatically on each push or pull request to the `main` branch. It uses `pytest` for testing.

## Running Tests

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run tests:
   ```bash
   pytest tests/
   ```