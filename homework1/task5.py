
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
    while k > 0:
        current_max = -math.inf
        for i in nums:
            if i > current_max:
                current_max = i
        nums[nums.index(current_max)] = -math.inf
        if current_max > 0:
            max_sum = max_sum + current_max
        else:
            if max_sum == 0:
                max_sum = max_sum + current_max
        k = k-1
    return max_sum
