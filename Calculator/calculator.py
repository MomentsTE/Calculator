"""
This module provides the Calculator class which uses basic operations
to perform calculations based on a given operator.
"""

from calculator.operations import add, subtract, multiply, divide


class Calculator:
    """
    Calculator class that performs calculations using supported operations.
    """

    def calculate(self, a: float, b: float, operator: str) -> float:
        if operator == "+":
            return add(a, b)
        elif operator == "-":
            return subtract(a, b)
        elif operator == "*":
            return multiply(a, b)
        elif operator == "/":
            return divide(a, b)
        else:
            raise ValueError(f"Unsupported operator: {operator}")
