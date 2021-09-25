from homework.homework7.task1 import backspace_compare


def test_nothing():
    assert backspace_compare("a", "a")


def test_backspace_at_start():
    assert backspace_compare("##a", "#a")


def test_easy():
    assert backspace_compare("abc#", 'abcd##')


def test_more_complicated():
    assert backspace_compare("abc#ef#", 'abcd##e')


def test_complicated():
    assert backspace_compare("abc#d###e", 'abcd####e')


def test_not_the_same():
    assert not backspace_compare("abc#d###eff#", 'abcd####e')
