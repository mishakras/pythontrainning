import io
import sys

from homework.homework3.task1 import cache


@cache(count=2)
def func3() -> str:
    return input('input was ')


@cache(count=2)
def func5() -> str:
    return input('input was ')


@cache(count=2)
def func6() -> str:
    return input('input was ')


def test_check_of_input():
    backup = sys.stdin
    sys.stdin = io.StringIO('1')
    func3()
    sys.stdin = io.StringIO('2')
    assert func3() == "1"
    sys.stdin = backup


def test_check_of_input_changed():
    backup = sys.stdin
    sys.stdin = io.StringIO('1')
    func5()
    func5()
    sys.stdin = io.StringIO('2')
    assert func5() == "2"
    sys.stdin = backup


def test_check_of_id():
    backup = sys.stdin
    sys.stdin = io.StringIO('1')
    assert id(func6()) == id(func6())
    sys.stdin = backup
