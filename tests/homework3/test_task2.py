import time

from homework.homework3 import task2


def test_fast_time():
    start = time.time()
    task2.calculate_all()
    assert time.time() - start < 60


#def test_slow_time():
#    start = time.time()
#    for i in range(50):
#        task2.slow_calculate(i)
#    assert time.time() - start > 60
