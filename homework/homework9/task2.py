"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with suppressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class Suppressor:
    def __init__(self, error_type):
        self.error_type = error_type

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == self.error_type:
            return True


@contextmanager
def suppressor(error_type):
    exc_type = 0
    try:
        pass
        yield
    except error_type:
        exc_type = 1
    finally:
        if exc_type == 1:
            return True


with Suppressor(IndexError):
    [][2]
with suppressor(IndexError):
    [][2]
