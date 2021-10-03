"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class Person:
    """Класс  реализует человека

        :param first_name: Имя
        :type first_name: str
        :param last_name: Фамилия
        :type last_name: str
        """
    def __init__(self, first_name, last_name):
        """Конструктор класса
                        """
        self.first_name = first_name
        self.last_name = last_name


class DeadlineError(Exception):
    """Класс, наследуемый от Exception, реализует ошибку при истечении
    сроков выполнения домашнего задания
    """
    pass


class Homework:
    """Класс реализует домашнее задание созданное классом Teacher
        для класса Student

        :param text: текст задания
        :type text: str
        :param created: время создания задания
        :type created: datetime.datetime
        :param deadline: предельная дата выполнения
        :type deadline: datetime.timedelta
        """
    def __init__(self, text, time):
        """Конструктор класса

                :param text: текст задания
                :type text: str
                :param time: Время выполнения в днях
                :type time: int
                """
        self.text = text
        self.created = datetime.datetime.now()
        self.deadline = datetime.timedelta(days=time)

    def is_active(self):
        """Проверка срока задания

        :return:True, если время выполнения не истекло, False иначе
        :rtype: bool
        """
        return datetime.datetime.now() < self.deadline + self.created


class Student(Person):
    """Класс реализует студента для выполнения домашней работы Homework

    :param first_name: Имя учителя
    :type first_name: str
    :param last_name: Фамилия учителя
    :type last_name: str
    """
    def __init__(self, first_name, last_name):
        """Конструктор класса
        """
        super().__init__(first_name, last_name)

    def do_homework(self, homework, solution):
        """Метод, реализующий выполнение домашнего задания

        :param homework: Домашняя работа, которую выполняет студент
        :type homework: Homework
        :param solution: Решение домашней работы
        :type solution: str
        :raise DeadlineError: если домашняя работа просрочена
        :return: Выполненная домашняя работа, выполненная студентом
        или ничего если работа просрочена
        :rtype: HomeworkResult, None
            """
        if homework.is_active():
            return HomeworkResult(homework, solution, self)
        else:
            raise DeadlineError("You are late")


class HomeworkResult:
    """Класс реализует выполненое домашнее задание классом Student

    :param homework: текст задания
    :type homework: Homework
    :param solution: время создания задания
    :type solution: str
    :param author: автор выполненного задания
    :type author: Student
    :param created: время выполнения задания
    :type created: datetime.datetime
    """
    def __init__(self, homework: Homework, solution: str, author: Student):
        """Конструктор класса с проверкой класса параметра homework
        :raise TypeError: если в homework передан другой класс
        """
        if not isinstance(homework, Homework):
            raise TypeError("That is not homework")
        self.homework = homework
        self.solution = solution
        self.student = author
        self.created = datetime.datetime.now()


class Teacher(Person):
    """Класс реализует учителя для создания домашнего задания в виде класса
    Homework

    :param first_name: Имя учителя
    :type first_name: str
    :param last_name: Фамилия учителя
    :type last_name: str
    :param homework_done: Параметр класса, хранящий все сделанные
    домашнии работы
    :type homework_done: defaultdict(list)
    """
    homework_done = defaultdict(list)

    def __init__(self, first_name, last_name):
        """Конструктор класса
        """
        super().__init__(first_name, last_name)

    @staticmethod
    def create_homework(text, time):
        """Метод, реализующий создание домашнего задания

        :param text: текст задания
        :type text: str
        :param time: Время выполнения в днях
        :type time: int
        :return: Домашнее задание с параметрами text, time
        :rtype: Homework
        """
        return Homework(text, time)

    @staticmethod
    def check_homework(homework: HomeworkResult):
        """Метод, реализующий проверку выполненного домашнего задания
        если домашнее задание выполненно правильно,
        добавляет его в выполненные
        :param homework: выполненное домашнее задание
        :type homework: HomeworkResult
        """
        if len(homework.solution) > 5:
            if Teacher.homework_done[homework.homework]\
                    .count(homework.solution) == 0:
                Teacher.homework_done[homework.homework]\
                    .append(homework.solution)

    @staticmethod
    def reset_results(homework: Homework = None):
        """Метод, реализующий очистку хранилища выполненных работ
        для работы homework или всего хранилища если вызывается без параметра
        :param homework: домашнее задание, defaults to None
        :type homework: Homework, None
        """
        if homework is None:
            Teacher.homework_done = defaultdict(list)
        else:
            Teacher.homework_done[homework] = []


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
