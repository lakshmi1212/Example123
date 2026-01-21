import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a,b,expected", [
    (3, 2, 1),
    (0, 0, 0),
    (-1, -1, 0),
    (200, 100, 100),
    (-5, 5, -10),
    (2.5, 3.5, -1.0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
