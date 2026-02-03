# Math Operations

This repository provides simple addition and subtraction functions with comprehensive tests and CI integration.

## Usage

```
from src.math_operations import add, subtract

print(add(2, 3))       # Output: 5
print(subtract(5, 2))  # Output: 3
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run all tests:

```
pytest tests/ -v --tb=short
```

## CI Workflow

The repository is set up for CI using GitHub Actions. Workflow file: `.github/workflows/ci.yml`
