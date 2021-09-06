"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
import math
from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    nums_in_list = Counter()
    minor = math.inf
    major = 0
    for i in inp:
        nums_in_list[i] += 1
    for i in nums_in_list.most_common():
        if i[1] < minor:
            minor = i[1]
            minor_int = i[0]
        if i[1] > major:
            major = i[1]
            major_int = i[0]
    return major_int, minor_int
