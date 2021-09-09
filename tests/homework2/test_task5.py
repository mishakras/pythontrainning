from homework.homework2.task5 import custom_range


def test_default():
    assert custom_range([2, 5, 7]) == [2, 5, 7]


def test_step2():
    assert custom_range([2, 5, 7], None, None, 2) == [2, 7]


def test_some_end():
    assert custom_range([1, 5, 8, 0, -1, 4, 3], 0) == [1, 5, 8]


def test_general():
    assert custom_range([1, 5, 8, 0, -1, 3], 5, -1, 2) == [5, 0]


def test_step_minus():
    assert custom_range([1, 5, 8, 0, -1, 3], 0, 5, -1) == [0, 8]


def test_general_string():
    assert custom_range("abcdxyzgh", 'b', 'z') == ['b', 'c', 'd', 'x', 'y']


def test_general_string_step2():
    assert custom_range("abcdxyzghnk", 'b', 'k', 2)\
           == ['b', 'd', 'y', 'g', 'n']


def test_general_string_no_start():
    assert custom_range("abcdxyzghnk", 'd') == ['a', 'b', 'c']
