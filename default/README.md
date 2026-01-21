# Example123

## Math Operations

This repository provides basic math operations (addition and subtraction) and their corresponding tests.

### Usage

```
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
```

### Testing

Install dependencies:
```
pip install -r default/requirements.txt
```

Run all tests:
```
pytest tests/ -v --tb=short
```

### CI Workflow

The CI pipeline is defined in `.github/workflows/ci.yml` and runs all tests on push and pull request events.
