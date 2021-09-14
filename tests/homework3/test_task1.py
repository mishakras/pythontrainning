import time

from mock import patch

from homework.homework3.task1 import cache


@cache(count=1)
def func(a: int, b: int) -> int:
    return a + 2*b


@cache(count=2)
def func2(a: int) -> int:
    time.sleep(1)
    return a


@cache(count=2)
def func3() -> str:
    return input('input was ')


@cache(count=2)
def func4(a: int) -> int:
    time.sleep(1)
    return a


def test_check_of_base_func():
    assert func(1, 1) == 3


def test_check_of_cache():
    func2(1)
    temp = time.time()
    func2(1)
    assert time.time() - temp < 1


def test_check_of_cache_to_many_calls():
    func4(1)
    func4(2)
    func4(3)
    func4(5)
    temp = time.time()
    func4(5)
    assert time.time() - temp > 0.5


def test_check_of_input():
    with patch('builtins.input') as MockClass:
        MockClass.return_value = '1'
        func3()
    with patch('builtins.input') as MockClass:
        MockClass.return_value = '2'
        assert func3() == "1"


def test_check_of_input_changed():
    with patch('builtins.input') as MockClass:
        MockClass.return_value = '1'
        func3()
    with patch('builtins.input') as MockClass:
        MockClass.return_value = '2'
        func3()
        assert func3() == "2"
