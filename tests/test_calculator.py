from calculator import add, subtract, multiply, division

def test_add():
    assert add(6, 6) == 12


def test_subtract():
    assert subtract(5, 4) == 1


def test_multiply():
    assert multiply(44, 2) == 88


def test_division():
    assert division(12, 3) == 4
