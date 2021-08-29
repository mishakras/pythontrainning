
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
    j = 0
    min_sum = -math.inf
    while i < len(nums):
        if nums[i] > 0:
            if j < k:
                temp_sum = temp_sum + nums[i]
                if temp_sum > max_sum:
                    max_sum = temp_sum
                j = j + 1
            else:
                temp_sum = temp_sum - nums[i-j] + nums[i]
                if temp_sum > max_sum:
                    max_sum = temp_sum
        else:
            j = 0
            temp_sum = 0
            if nums[i] > min_sum:
                min_sum = nums[i]
        i = i + 1
    if min_sum == -math.inf:
        min_sum = 0
    if max_sum > 0:
        return max_sum
    else:
        return min_sum
