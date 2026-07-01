import pytest

from calculator import add, subtract, multiply, division, calculate

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
    assert division(50, 5) == 10
    assert division(0, 9) == 0
    assert division(-15, 5) == -3


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)


def calculate(x, y, operation):
        if operation == "+":
            return add(x, y)
        elif operation == "-":
            return subtract(x, y)
        elif operation == "*":
            return  multiply(x, y)
        elif operation == "/":
            return division(x, y)
        return None



def test_calculate_add():
    assert calculate(25, 5, "+") == 30
