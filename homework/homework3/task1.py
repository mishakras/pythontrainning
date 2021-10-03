"""
In previous homework task 4, you wrote a cache function that
 remembers other function output value. Modify it to be
  a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:
@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2,
     use raw_input() instead

f()
? 1
'1'
f()     # will remember previous value
'1'
f()     # but use it up to two times only
'1'
f()
? 2
'2'
"""
from typing import Callable


def cache(count: int):
    def cache_maker(func: Callable) -> Callable:
        lst = {-1: 1}

        def fin():
            if count > lst.get(-1):
                if lst.get(count):
                    lst[-1] += 1
                    return lst.get(count)
            lst[-1] = 1
            a = func()
            lst[count] = a
            return a
        return fin
    return cache_maker
