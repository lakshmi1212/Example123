# Math Operations Example

This repository provides basic math operations (addition and subtraction) with automated testing and CI/CD workflow integration.

## Folder Structure

- `src/`: Source code for math operations
- `tests/`: Pytest-based unit tests
- `default/`: Project metadata, requirements, and documentation

## Usage

1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Use the functions in `src/math_operations.py`:
   ```python
   from src.math_operations import add, subtract
   print(add(2, 3))        # Output: 5
   print(subtract(5, 2))   # Output: 3
   ```

## Running Tests

Run all tests with:
```bash
pytest tests/ -v --tb=short
```

## CI/CD

This project is designed for integration with GitHub Actions using a workflow file at `.github/workflows/ci.yml`.
