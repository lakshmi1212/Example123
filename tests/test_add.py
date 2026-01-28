import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-4, -7) == -11

def test_add_mixed_sign_numbers():
    assert add(-2, 6) == 4

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
