from homework.homework2.task4 import cache


def func(a: int, b: int) -> bool:
    return a+b > b*b


def func2(a: int, b: int, c: int) -> bool:
    return a*c+b > c+b*b


def test_1_run():
    fin = cache(func)
    assert not fin(1, 2)[1]


def test_2_runs():
    fin = cache(func)
    fin(1, 2)
    assert fin(5, 1)[0] == [False, True]


def test_more_runs():
    fin = cache(func2)
    fin(1, 2, 3)
    fin(1, 2, 10)
    assert fin(5, 1, 1)[0] == [False, False, True]
