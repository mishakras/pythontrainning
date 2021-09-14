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
        lst = {}
        temp = []

        def fin(*args):
            if len(args) != 0:
                if lst.get(args):
                    return lst.get(args)
                a = func(*args)
                if len(lst) < count:
                    lst[args] = a
            else:
                if len(temp) == 0:
                    a = func()
                    temp.append(a)
                    return temp[0]
                if len(temp) <= count:
                    temp.append('1')
                    return temp[0]
                a = func()
                temp.append(a)
            return a
        return fin
    return cache_maker
