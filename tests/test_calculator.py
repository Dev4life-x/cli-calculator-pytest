import json

import pytest

from calculator import add, subtract, multiply, division, calculate, save_history, load_history


def test_add():
    assert add(6, 6) == 12
    assert add(0, 0) == 0
    assert add(-4, 4) == 0


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


def test_save_history(tmp_path):
    filename = tmp_path / "test_history.json"
    history = ["30 + 5 = 35"]

    save_history(history, filename)

    with open(filename, "r") as file:
        data = json.load(file)


    assert data == history 


def test_load_history(tmp_path):
    filename = tmp_path / "test_history.json"
    history = ["50 + 55 = 105"]

    with open(filename, "w") as file:
        json.dump(history, file)

    assert load_history(filename) == history


def test_calculate_add():
    assert calculate(25, 5, "+") == 30


def test_calculate_subtract():
    assert calculate(44, 4, "-") == 40


def test_calculate_multiply():
    assert calculate(55, 6, "*") == 330


def test_calculate_division():
    assert calculate(44, 11, "/") == 4.0


def test_calculate_invalid_operation():
    assert calculate(34, 7, "%") is None