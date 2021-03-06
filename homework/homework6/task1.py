"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """Декоратор  добавляющий классу счётчик созданных экземпляров

    :param cls: Класс для декорирования
    :return: Декорированный класс
    """
    setattr(cls, '_counter', 0)
    original_init = cls.__init__

    def __init__(*args, **kwargs):
        """Новый конструктор для clc

        """
        original_init(*args, **kwargs)
        cls._counter += 1

    @staticmethod
    def get_created_instances():
        """Метод, возвращающий количество экземпляров класса

        :return: количество экземпляров класса
        :rtype int
        """
        return cls._counter

    @staticmethod
    def reset_instances_counter():
        """Метод, обнуляющий количество экземпляров класса и
         возвращающий количество экземпляров класса до обнуления

        :return: количество экземпляров класса до обнуления
        :rtype int
        """
        temp = cls._counter
        cls._counter = 0
        return temp

    setattr(cls, '__init__', __init__)
    setattr(cls, 'get_created_instances', get_created_instances)
    setattr(cls, 'reset_instances_counter', reset_instances_counter)
    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user: User
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
    print(User.get_created_instances())
