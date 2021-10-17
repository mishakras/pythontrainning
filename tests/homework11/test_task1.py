from homework.homework11.task1 import SimplifiedEnum


def test_one_class():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    c = ColorsEnum()
    assert c.BLUE == 'BLUE'


def test_other_class():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    c = SizesEnum()
    assert c.XS == 'XS'
