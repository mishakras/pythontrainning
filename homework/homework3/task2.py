import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data)), value


def gen():
    i = 0
    while True:
        i += 1
        yield i
        if i == 501:
            break


def calculate_all():
    with Pool(500) as p:
        p.map(slow_calculate, gen())
