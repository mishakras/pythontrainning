"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
import copy
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    final = [[]]
    for lists in args:
        temp1 = []
        for i in lists:
            temp2 = copy.deepcopy(final)
            for j in temp2:
                j.append(i)
                temp1.append(j)
        final = copy.deepcopy(temp1)
    return final
