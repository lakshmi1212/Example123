# Example123: Math Operations

## Overview
This repository provides basic math operations (addition and subtraction) and includes comprehensive pytest test coverage.

## Folder Structure
- `src/`: Production Python code for math operations
- `tests/`: Pytest test files for all operations
- `default/`: Metadata, requirements, and documentation

## Usage

### Install Dependencies
```bash
pip install -r default/requirements.txt
```

### Run Tests
```bash
pytest tests/ -v --tb=short
```

## CI/CD Workflow
The CI pipeline is defined in `.github/workflows/ci.yml` and runs all tests on every push or pull request to `main`.

## Python Version
Python 3.10 is required.
