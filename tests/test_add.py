import pytest
from src.math_operations import add

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
    (100, 200, 300),
    (-5, 5, 0),
    (2.5, 3.5, 6.0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
