from homework.homework5.task2 import custom_sum


def test_of__doc__():
    assert custom_sum.__doc__ == \
           "This function can sum any objects which have __add___"


def test_of__name__():
    assert custom_sum.__name__ == "custom_sum"


def test_of_sum():
    assert custom_sum.__original_func(1, 1, 1) == 3
