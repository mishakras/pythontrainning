import hashlib
import random
import struct
import time
from multiprocessing import Process


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data)), value


def calculate_all():
    procs = []
    for i in range(500):
        p = Process(target=slow_calculate, args=(i, ))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()
