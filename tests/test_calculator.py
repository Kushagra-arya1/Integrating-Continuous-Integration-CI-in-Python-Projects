"""Automated test suite for mini_calc module."""
import pytest
from mini_calc.calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    is_even,
    factorial,
    average,
    percentage,
)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (-4, -6, -10),
        (2.5, 3.5, 6.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 4, 6),
        (5, 10, -5),
        (-3, -3, 0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 7, 21),
        (-2, 4, -8),
        (0, 100, 0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        divide(10, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True
    with pytest.raises(TypeError):
        is_even(3.5)
    with pytest.raises(TypeError):
        is_even(True)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError, match="Factorial is undefined"):
        factorial(-1)
    with pytest.raises(TypeError):
        factorial(3.2)


def test_average():
    assert average([10, 20, 30]) == 20.0
    assert average([5]) == 5.0
    with pytest.raises(ValueError, match="Cannot calculate average"):
        average([])


def test_percentage():
    assert percentage(25, 100) == 25.0
    assert percentage(1, 2) == 50.0
    with pytest.raises(ZeroDivisionError):
        percentage(50, 0)
