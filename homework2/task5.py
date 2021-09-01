"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""

from typing import List, Any, Sequence


def custom_range(it: Sequence, start: Any = None, end: Any = None, step: int = 1) -> List:
    flag = False
    final = []
    if step == 0:
        final.append("Error, step must not be 0")
        return final
    if step < 0:
        it = reversed(it)
        step = -step
    k = step
    if start is None:
        flag = True
    for i in it:
        if start is not None and start == i:
            flag = True
        if end is not None and end == i:
            flag = False
        if flag:
            if k == step:
                final.append(i)
                k = 1
            else:
                k += 1
    return final
