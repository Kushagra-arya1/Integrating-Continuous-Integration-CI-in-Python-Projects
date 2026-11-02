"""Core Calculator Operations with minimal code and 100% test coverage."""
from typing import Sequence, Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of two numbers."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return quotient of a / b. Raises ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """Return base raised to exponent."""
    return base ** exponent


def is_even(n: int) -> bool:
    """Check if an integer is even."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer.")
    return n % 2 == 0


def factorial(n: int) -> int:
    """Calculate factorial of non-negative integer n."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def average(numbers: Sequence[Number]) -> float:
    """Calculate arithmetic mean of a sequence of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of an empty sequence.")
    return sum(numbers) / len(numbers)


def percentage(part: Number, total: Number) -> float:
    """Calculate percentage of part relative to total."""
    if total == 0:
        raise ZeroDivisionError("Total cannot be zero for percentage.")
    return (part / total) * 100.0
