from homework.homework1.task2 import check_fibonacci


def test_too_small():
    assert check_fibonacci([1])


def test_small():
    assert check_fibonacci([1, 1])


def test_positive_case():
    assert check_fibonacci([1, 1, 2, 3, 5])


def test_negative_case_random_numbers():
    assert not check_fibonacci([2, 1, 3, 4, 7])


def test_negative_case():
    assert not check_fibonacci([1, 2, 3, 4, 5])
