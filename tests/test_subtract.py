import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_mixed_signs():
    assert subtract(-2, 3) == -5
    assert subtract(3, -2) == 5

def test_subtract_float():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)

def test_subtract_large_numbers():
    assert subtract(1e10, 1e9) == 9e9
