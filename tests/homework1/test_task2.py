from homework1.task2 import check_fibonacci


def test_too_small():
    assert check_fibonacci([1, 2])


def test_positive_case_base():
    assert check_fibonacci([1, 1, 2, 3, 5])


def test_positive_case_with_negatives():
    assert check_fibonacci([5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5])


def test_positive_case_random_numbers():
    assert check_fibonacci([2, 1, 3, 4, 7])


def test_negative_case():
    assert not check_fibonacci([1, 2, 3, 4, 5])


def test_negative_case_2():
    assert not check_fibonacci([2, 1, 3, 4, 7, 8])
