from homework2.task3 import combinations


def test_too_small():
    assert combinations([1]) == [[1]]


def test_positive_numbers():
    assert combinations([1, 2]) == [[1], [2]]


def test_negative_numbers():
    assert combinations([1, 2], [1]) == [[1, 1], [2, 1]]


def test_positive_and_negative_numbers():
    assert combinations([1, 2], ['a'], ['s', ' '])\
           == [[1, 'a', 's'], [2, 'a', 's'], [1, 'a', ' '], [2, 'a', ' ']]
