import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_positive_and_negative():
    assert subtract(-2, 3) == -5

def test_subtract_floats():
    assert subtract(5.5, 2.1) == pytest.approx(3.4)
