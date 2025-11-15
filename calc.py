"""Simple calculator module with create, add and subtract functions.

Functions:
- create(value=0): validate and return a numeric value
- add(a, b): return a + b
- subtract(a, b): return a - b
"""
from typing import Union

Number = Union[int, float]

def create(value: Number = 0) -> Number:
    """Return a numeric value after validating the input.

    Raises TypeError if value is not int or float.
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be int or float")
    return value

def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """Return the difference a - b."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b."""
    return a * b

def divide(a: Number, b: Number) -> Number:
    """Return the division a / b.

    Raises ZeroDivisionError if `b` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
