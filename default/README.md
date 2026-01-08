# Math Operations

This project provides basic math operations including addition and subtraction. It includes test automation and CI/CD integration.

## Structure

- `src/math_operations.py`: Contains the logic for addition and subtraction.
- `tests/`: Contains unit tests for the math operations.
- `math.json`: Metadata for CI/CD workflows.
- `requirements.txt`: Dependencies for the project.

## Usage

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run tests using `pytest`.

## CI/CD Workflow

The repository is configured for a CI/CD workflow triggered on push and pull requests to the `main` branch. It ensures all tests pass before merging changes.
