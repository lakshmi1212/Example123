import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(3, 2) == 5

def test_add_negative_numbers():
    assert add(-3, -2) == -5

def test_add_positive_and_negative():
    assert add(3, -2) == 1

def test_add_zero():
    assert add(0, 5) == 5
