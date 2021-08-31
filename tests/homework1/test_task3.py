from homework1.task3 import find_maxi_and_min


def test_too_small():
    assert find_maxi_and_min("tests/homework1/small.txt") == (1, 1)


def test_positive_numbers():
    assert find_maxi_and_min("tests/homework1/pos.txt") == (0, 15)


def test_negative_numbers():
    assert find_maxi_and_min("tests/homework1/neg.txt") == (-15, -1)


def test_positive_and_negative_numbers():
    assert find_maxi_and_min("tests/homework1/pos_neg.txt") == (-10, 15)
