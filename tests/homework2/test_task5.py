from homework2.task5 import custom_range


def test_no_step():
    assert custom_range([1, 2, 3], 0, 2, 0) == ['Error, step must not be 0']


def test_default():
    assert custom_range([2, 5, 7]) == [2, 5, 7]


def test_step2():
    assert custom_range([2, 5, 7], step=2) == [2, 7]


def test_some_end():
    assert custom_range([1, 5, 8, 0, -1, 4, 3], end=0) == [1, 5, 8]


def test_general():
    assert custom_range([1, 5, 8, 0, -1, 3], 5, -1, 2) == [5, 0]


def test_step_minus():
    assert custom_range([1, 5, 8, 0, -1, 3], 0, 5, -1) == [0, 8]
