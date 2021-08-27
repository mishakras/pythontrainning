"""
Write down the function, which reads input line-by-line, and
find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
import math
from typing import Tuple


def find_maxi_and_min(file_name: str) -> Tuple[int, int]:
    minint = math.inf
    maxint = -math.inf
    with open(file_name) as fi:
        for line in fi:
            length = len(line)
            i = 0
            while i < length:
                s_int = ''
                a = line[i]
                while '0' <= a <= '9' or a == "-":
                    s_int += a
                    i += 1
                    if i < length:
                        a = line[i]
                    else:
                        break
                i += 1
                if s_int != '':
                    if int(s_int) < minint:
                        minint = int(s_int)
                    if int(s_int) > maxint:
                        maxint = int(s_int)
    return minint, maxint
