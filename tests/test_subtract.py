import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6

def test_subtract_negative_numbers():
    assert subtract(-5, -2) == -3

def test_subtract_mixed_sign_numbers():
    assert subtract(-3, 7) == -10
    assert subtract(7, -3) == 10

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5

def test_subtract_large_numbers():
    assert subtract(2000000, 1000000) == 1000000
