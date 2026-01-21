# Math Operations

This repository provides basic math operations (addition and subtraction) with automated tests and CI integration.

## Usage

```
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run tests:

```
pytest tests/ -v --tb=short
```

## CI/CD Workflow

A GitHub Actions workflow is expected in `.github/workflows/ci.yml` to run tests on each push or pull request.
