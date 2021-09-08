import time

from homework import homework3 as task2


def test1():
    start = time.time()
    task2.calculate_all()
    assert time.time() - start < 3600
