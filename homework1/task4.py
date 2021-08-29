"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are
    such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of
    N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int],
                      d: List[int]) -> int:
    amount = 0
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    n = len(a)
    if a[0] + b[0] + c[0] + d[0] > 0:
        print("a")
        return 0
    if a[n-1] + b[n-1] + c[n-1] + d[n-1] < 0:
        print("b")
        return 0
    for i in a:
        if -d[0] - b[0] - c[0] < i or i < -d[n-1] - b[n-1] - c[n-1]:
            print("c")
            break
        for j in b:
            if -d[0] - c[0] < i + j or i + j < -d[n-1] - c[n-1]:
                print("d")
                break
            for k in c:
                if -d[0] < i + j + k or i + j + k < -d[n - 1]:
                    print("e")
                    break
                for g in d:
                    if i + j + k + g > 0:
                        print("k")
                        break
                    if i + j + k + g == 0:
                        amount = amount + 1
    return amount
