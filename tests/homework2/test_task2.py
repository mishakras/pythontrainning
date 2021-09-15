from homework.homework2.task2 import major_and_minor_elem


def test_too_small():
    assert major_and_minor_elem([1]) == (1, 1)


def test_small():
    assert major_and_minor_elem([1, 2, 1]) == (1, 2)


def test_base():
    assert major_and_minor_elem([1, 1, 1, 1, 2, 3, 5]) == (1, 2)
