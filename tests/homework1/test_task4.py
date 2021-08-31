from homework1.task4 import check_sum_of_four


def test_no_zeros():
    assert check_sum_of_four([1], [1], [1], [1]) == 0


def test_all_zeros():
    assert check_sum_of_four([0], [0], [0], [0]) == 1


def test_some_zero_sums():
    assert check_sum_of_four([1, 1], [-1, 100], [0, 100], [0, 100]) == 2
