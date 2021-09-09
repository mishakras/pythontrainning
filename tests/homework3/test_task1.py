import time

from homework.homework3.task1 import cache


def func(a: int, b: int) -> int:
    return a + 2*b


def func2(a: int) -> int:
    time.sleep(1)
    return a


def test_check_of_base_func():
    fin = cache(func, 1)
    assert fin(1, 1) == 3


def test_check_of_cache():
    fin = cache(func2, 1)
    fin(5)
    temp = time.time()
    fin(5)
    assert time.time() - temp < 1


def test_check_of_cache_to_many_calls():
    fin = cache(func2, 2)
    fin(1)
    fin(2)
    fin(3)
    fin(5)
    temp = time.time()
    fin(5)
    assert time.time() - temp > 0.5
