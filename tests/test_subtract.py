import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(10, 5) == 5

def test_subtract_negative_numbers():
    assert subtract(-10, -5) == -5

def test_subtract_mixed_numbers():
    assert subtract(-5, 10) == -15

def test_subtract_zero():
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5