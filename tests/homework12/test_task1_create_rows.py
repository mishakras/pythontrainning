import homework.homework12.task1_create_rows as task1
from homework.homework12.task1_tables import (Homework, HomeworkResult,
                                              Student, Teacher)

with task1.session_scope() as session:
    student = task1.make_student('Michail', 'Kras')
    teacher = task1.make_teacher('Daniil', 'Shadrin')
    homework = task1.make_homework(teacher, 'Read docs', 5)
    task1.make_homework_result(teacher, homework, student,
                               'I have done this hw')


def test_read_student():
    flag = False
    with task1.session_scope() as session:
        q = session.query(Student.name).all()
        for i in q:
            print(i)
            if i == ('Michail',):
                flag = True
    assert flag


def test_read_teacher():
    flag = False
    with task1.session_scope() as session:
        q = session.query(Teacher.name).all()
        for i in q:
            print(i)
            if i == ('Daniil',):
                flag = True
    assert flag


def test_read_homework():
    flag = False
    with task1.session_scope() as session:
        q = session.query(Homework.name).all()
        for i in q:
            print(i)
            if i == ('Read docs',):
                flag = True
    assert flag


def test_read_homeworkresults():
    flag = False
    with task1.session_scope() as session:
        q = session.query(HomeworkResult.solution).all()
        for i in q:
            print(i)
            if i == ('I have done this hw',):
                flag = True
    assert flag
