from homework1.task4 import check_sum_of_four


def test_too_small():
    assert check_sum_of_four([1], [1], [1], [1]) == 0


def test_positive_case_base():
    assert check_sum_of_four([0], [0], [0], [0]) == 1


def test_positive_case_random_numbers():
    assert check_sum_of_four([1, 1], [-1], [0], [0]) == 2
