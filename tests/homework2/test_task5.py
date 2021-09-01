from homework2.task5 import custom_range


def test_no_subarray():
    assert custom_range([1, 2, 3], 0, 2, 0) == ['Error, step must not be 0']


def test_max_in_array():
    assert custom_range([2, 5, 7], step=2) == [2, 7]


def test_some_subarray():
    assert custom_range([1, 5, 8, 0, -1, 4, 3], end=0) == [1, 5, 8]


def test_subarray_with_repeating_numbers():
    assert custom_range([1, 5, 8, 0, -1, 3], 0, 5, -1) == [0, 8]

