import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_mixed_numbers():
    assert subtract(5, -3) == 8

def test_subtract_zero():
    assert subtract(5, 0) == 5
