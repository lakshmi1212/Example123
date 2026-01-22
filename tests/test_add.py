import pytest
from src.math_operations import add

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
    (-5, 5, 0),
    (1.5, 2.5, 4.0),
    (1000000, 2000000, 3000000)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
