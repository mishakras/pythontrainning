
"""
Given a list of integers numbers "nums".
You need to find a sub-array with length
    less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
import math
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    temp_sum = 0
    i = 0
    min_sum = -math.inf
    for length in nums:
        for j in range(k):
            for k in nums[i:j]:
                temp_sum = temp_sum + k
            if temp_sum > max_sum:
                max_sum = temp_sum
        i += 1
    for j in nums:
        if min_sum < j < 0:
            min_sum = j
    if max_sum > 0:
        return max_sum
    else:
        return min_sum
