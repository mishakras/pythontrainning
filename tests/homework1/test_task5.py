from homework.homework1.task5 import find_maximal_subarray_sum


def test_no_subarray():
    assert find_maximal_subarray_sum([1, 2, 3], 0) == 0


def test_max_in_array():
    assert find_maximal_subarray_sum([2, 5, 7], 1) == 7


def test_some_subarray():
    assert find_maximal_subarray_sum([1, 5, 8, 0, -1, 4, 3], 4) == 14


def test_subarray_with_repeating_numbers():
    assert find_maximal_subarray_sum([1, 5, 8, 0, 8, 8], 3) == 16


def test_subarray_with_only_negatives():
    assert find_maximal_subarray_sum([-1, -5, -8, -7, -2], 3) == -1
