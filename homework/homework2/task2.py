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
from typing import List


def major_and_minor_elem(inp: List):
    temp = {}
    for i in inp:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    maximum = 0
    minimum = math.inf
    for key in temp:
        if temp[key] > maximum:
            if temp[key] > len(inp)//2:
                maximum = temp[key]
                major = key
        if temp[key] < minimum:
            minimum = temp[key]
            minor = key
    return major, minor
