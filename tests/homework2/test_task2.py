from homework2.task2 import major_and_minor_elem


def test_positive_case1():
    assert major_and_minor_elem([1]) == (1, 1)


def test_positive_case2():
    assert major_and_minor_elem([1, 2]) == (1, 1)


def test_positive_case3():
    assert major_and_minor_elem([1, 1, 2, 3, 5]) == (1, 2)


