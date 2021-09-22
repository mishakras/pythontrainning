from homework.homework6.task1 import instances_counter


@instances_counter
class Temp:
    pass


def test_no_instances():
    assert Temp.get_created_instances() == 0


def test_some_instances():
    temp1, temp2, temp3 = Temp(), Temp(), Temp()
    assert Temp.get_created_instances() == 3


def test_delete_some_instances():
    temp1, temp2, temp3 = Temp(), Temp(), Temp()
    Temp.reset_instances_counter()
    assert Temp.get_created_instances() == 0



