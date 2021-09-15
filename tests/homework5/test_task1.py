import datetime

from homework.homework5.task1 import Teacher, Homework, Student


def test_student_first_name():
    s = Student("Misha", "Kras")
    assert s.first_name == "Misha"


def test_student_last_name():
    s = Student("Misha", "Kras")
    assert s.last_name == "Kras"


def test_teacher_last_name():
    t = Teacher("Misha", "Kras")
    assert t.last_name == "Kras"


def test_teacher_first_name():
    t = Teacher("Misha", "Kras")
    assert t.first_name == "Misha"


def test_homework_text():
    h = Homework("test", 3)
    assert h.text == "test"


def test_homework_deadline():
    h = Homework("test", 3)
    assert h.deadline == datetime.timedelta(days=3)


def test_homework_is_active():
    h = Homework("test", 3)
    assert h.is_active()


def test_homework_is_not_active():
    h = Homework("test", 0)
    assert not h.is_active()


def test_teacher_create_homework():
    h = Teacher.create_homework("test", 3)
    assert h.text == "test"


def test_student_create_homework_active():
    h = Teacher.create_homework("test", 3)
    s = Student("Misha", "Kras")
    assert s.do_homework(h) == h


def test_student_create_homework_not_active():
    h = Teacher.create_homework("test", 0)
    s = Student("Misha", "Kras")
    assert s.do_homework(h) is None
