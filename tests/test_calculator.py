import pytest

from calculator import add, subtract, multiply, division

def test_add():
    assert add(6, 6) == 12
    assert add(0, 0) == 0
    assert add (-4, 4) == 0


def test_subtract():
    assert subtract(5, 4) == 1
    assert subtract(0, 0) == 0
    assert subtract(-3, 3) == -6


def test_multiply():
    assert multiply(44, 2) == 88
    assert multiply(0, 0) == 0
    assert multiply(-9, 2) == -18


def test_division():
    division(50, 5) == 10
    division(0, 9) == 0
    division(-15, 5) == -3


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)



