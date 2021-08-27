from homework1.task3 import find_maximum_and_minimum


def test_too_small():
    assert find_maximum_and_minimum("tests/homework1/test_task3_too_small.txt") == (1, 1)


def test_positive_numbers():
    assert find_maximum_and_minimum("tests/homework1/test_task3_positive_numbers.txt") == (0, 15)


def test_negative_numbers():
    assert find_maximum_and_minimum("tests/homework1/test_task3_negative_numbers.txt") == (-15, -1)


def test_positive_and_negative_numbers():
    assert find_maximum_and_minimum("tests/homework1/test_task3_positive_and_negative_numbers.txt") == (-10, 15)
