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
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    minor = math.inf
    major = 0
    nums_in_list = []
    amount_nums_in_list = []
    for i in inp:
        if nums_in_list.count(i) == 0:
            amount_nums_in_list.append(inp.count(i))
            nums_in_list.append(i)
    for index, i in enumerate(nums_in_list):
        c = amount_nums_in_list[index]
        if c < minor:
            minor = c
            minor_int = i
        if c > major:
            major = c
            major_int = i
    return major_int, minor_int
