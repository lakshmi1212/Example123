import pytest
from src.math_operations import subtract

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 0) == 0
    assert subtract(200, 100) == 100