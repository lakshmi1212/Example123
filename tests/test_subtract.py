import pytest
from src.math_operations import subtract

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(100, 50) == 50
    assert subtract(-10, 10) == -20
