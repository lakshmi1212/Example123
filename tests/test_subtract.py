import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (0, 0, 0),
    (-1, 1, -2),
    (2.5, 1.5, 1.0),
    (-7, -3, -4),
    (1000000, 500000, 500000),
    (0, 5, -5),
    (5, 0, 5),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
