"""
This module contains basic mathematical operations for the calculator.
Each function performs a single operation and returns the result.
"""


def add(a: float, b: float) -> float:
    """
    this will return the sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    this will return the result of subtracting b from a.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    this will return the product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    this will return the result of dividing a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
