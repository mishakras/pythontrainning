import time

from homework.homework2.task4 import cache


def func(a: int, b: int) -> int:
    return a + 2*b


def func2(a: int) -> int:
    time.sleep(5)
    return a


def test_check_of_base_func():
    fin = cache(func)
    assert fin(1, 1) == 3


def test_check_of_cache():
    fin = cache(func2)
    fin(5)
    temp = time.time()
    fin(5)
    assert time.time() - temp < 1
