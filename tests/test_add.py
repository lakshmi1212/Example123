import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_mixed_sign():
    assert add(-2, 3) == 1
    assert add(2, -3) == -1

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
