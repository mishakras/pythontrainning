from homework.homework9.task2 import suppressor, Suppressor


def test_suppressor_class():
    with Suppressor(IndexError):
        [][2]


def test_suppressor_function():
    with suppressor(IndexError):
        [][2]
