from homework3.task4 import is_armstrong


def test_positive_small():
    assert is_armstrong(9)


def test_positive():
    assert is_armstrong(153)


def test_negative():
    assert not is_armstrong(20)
