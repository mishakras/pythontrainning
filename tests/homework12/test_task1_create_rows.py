import homework.homework12.task1_create_rows as task1
from homework.homework12.task1_tables import (Homework, HomeworkResult,
                                              Student, Teacher)

with task1.session_scope() as session:
    student = task1.make_student('Alexander', 'Kras')
    student2 = task1.make_student('Michail', 'Kras')
    teacher = task1.make_teacher('Daniil', 'Shadrin')
    homework = task1.make_homework('Read docs', 5)
    task1.make_homework_result(homework, student,
                               'I have done this hw')


def test_read_student():
    with task1.session_scope() as session:
        q = session.query(Student).filter(Student.name == 'Michail').all()
        assert bool(q)


def test_read_another_student():
    with task1.session_scope() as session:
        q = session.query(Student).filter(Student.name == 'Alexander').all()
        assert bool(q)


def test_read_wrong_student():
    with task1.session_scope() as session:
        q = session.query(Student).filter(Student.name == 'Daniil').all()
        assert not bool(q)


def test_read_teacher():
    with task1.session_scope() as session:
        q = session.query(Teacher).filter(Teacher.name == 'Daniil').all()
        assert bool(q)


def test_read_homework():
    with task1.session_scope() as session:
        q = session.query(Homework).all()
        for i in q:
            if i.name == 'Read docs':
                return
    assert False


def test_read_homeworkresults():
    with task1.session_scope() as session:
        q = session.query(HomeworkResult).all()
        for i in q:
            if i.solution == 'I have done this hw':
                return
    assert False
