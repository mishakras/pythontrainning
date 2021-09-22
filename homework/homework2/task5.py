"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g')
== ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p')
== ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2)
== ['p', 'n', 'l', 'j', 'h']
"""
from typing import List, Sequence


def custom_range(iterable: Sequence, *args) -> List:
    if len(args) == 0:
        start, stop, step = None, None, 1
    elif len(args) == 1:
        start, stop, step = None, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    else:
        start, stop, step = args[0], args[1], args[2]
    flag = False
    final = []
    if step < 0:
        iterable = reversed(iterable)
        step = -step
    k = step
    if start is None:
        flag = True
    for i in iterable:
        if start is not None and start == i:
            flag = True
        if stop is not None and stop == i:
            flag = False
        if flag:
            if k == step:
                final.append(i)
                k = 1
            else:
                k += 1
    return final
