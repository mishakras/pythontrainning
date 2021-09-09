import time

from homework.homework3 import task2


def test1():
    start = time.time()
    task2.calculate_all()
    assert time.time() - start < 3600
