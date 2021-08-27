"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return True
    for item in data:
        if data.index(item) > 1:
            if item != data[data.index(item)-1]+data[data.index(item)-2]:
                return False
    return True
