import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(10, 5) == 5

def test_subtract_negative_numbers():
    assert subtract(-10, -5) == -5

def test_subtract_mixed_numbers():
    assert subtract(10, -5) == 15

def test_subtract_with_zero():
    assert subtract(0, 5) == -5