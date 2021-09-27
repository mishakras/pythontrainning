from homework.homework2.task3 import combinations


def test_small():
    assert combinations([1]) == [[1]]


def test_1_list():
    assert combinations([1, 2]) == [[1], [2]]


def test_base():
    assert combinations([1, 2], [1]) == [[1, 1], [2, 1]]


def test_complex():
    assert combinations([1, 2], ['a'], ['s', ' '])\
           == [[1, 'a', 's'], [2, 'a', 's'], [1, 'a', ' '], [2, 'a', ' ']]
