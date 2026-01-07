import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-3, -5) == -8

def test_add_mixed_numbers():
    assert add(-3, 5) == 2

def test_add_zero():
    assert add(0, 5) == 5
    assert add(3, 0) == 3