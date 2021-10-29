from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

import homework.homework12.task1_tables as task1


@contextmanager
def session_scope():
    session_in_scope = sessionmaker(bind=task1.engine)
    session_in_scope = session_in_scope()
    try:
        yield session_in_scope
        session_in_scope.commit()
    except Exception:
        session_in_scope.rollback()
        raise
    finally:
        session_in_scope.close()


def make_student(name, last_name):
    student = task1.Student(
        name=name,
        last_name=last_name
    )
    session.add(student)
    session.commit()
    return student


def make_teacher(name, last_name):
    teacher = task1.Teacher(
        name=name,
        last_name=last_name
    )
    session.add(teacher)
    session.commit()
    return teacher


def make_homework(text, time):
    homework = task1.create_homework(
        text=text,
        time=time
    )
    session.add(homework)
    session.commit()
    return homework


def make_homework_result(homework: task1.Homework, student: task1.Student,
                         solution):
    homework_result = task1.do_homework(student, homework, solution)
    task1.check_homework(homework_result)
    return homework_result


with session_scope() as session:
    pass
