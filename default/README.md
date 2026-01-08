# Math Operations

This repository provides basic math operations such as addition and subtraction.

## Usage

### Add Function
```python
from src.math_operations import add
result = add(2, 3)
print(result)  # Output: 5
```

### Subtract Function
```python
from src.math_operations import subtract
result = subtract(5, 3)
print(result)  # Output: 2
```

## Testing

Run the following command to execute tests:
```bash
pytest tests/
```

## Workflow

This repository is integrated with a CI pipeline that runs tests automatically on every push or pull request to the `main` branch.