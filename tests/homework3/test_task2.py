import time

import homework3.task2 as task2


def test1():
    start = time.time()
    task2.calculate_all()
    assert time.time()-start < 3600
