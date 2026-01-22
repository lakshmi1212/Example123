import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a,b,expected", [
    (3, 2, 1),
    (0, 0, 0),
    (-1, -1, 0),
    (-5, 5, -10),
    (2.5, 1.5, 1.0),
    (1000000, 2000000, -1000000)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
