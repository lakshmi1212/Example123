# Example123

This repository contains basic math operations implemented in Python, with automated tests and CI/CD workflow integration.

## Features
- Addition and subtraction functions
- Pytest-based tests
- GitHub Actions CI workflow (see .github/workflows/ci.yml)

## Usage

```python
from src.math_operations import add, subtract

print(add(2, 3))        # 5
print(subtract(5, 2))   # 3
```

## Running Tests

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run tests:

```bash
pytest tests/ -v --tb=short
```
