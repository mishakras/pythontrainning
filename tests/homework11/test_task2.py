from homework.homework11.task2 import Order


def morning_discount(price):
    return price*0.25


def elder_discount(price):
    return price * 0.9


def some_discount(price):
    if price > 200:
        return price * 0.9
    else:
        return price * 0.5


def test_one_discount():
    order1 = Order(100, morning_discount)
    assert order1.final_price() == 75


def test_other_discount():
    order2 = Order(10, elder_discount)
    assert order2.final_price() == 1


def test_some_discount_big_price():
    order3 = Order(300, some_discount)
    assert order3.final_price() == 30


def test_some_discount_small_price():
    order3 = Order(60, some_discount)
    assert order3.final_price() == 30
