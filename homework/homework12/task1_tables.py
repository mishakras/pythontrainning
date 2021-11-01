"""
Using ORM framework of your choice, create models classes
 created in Homework 6 (Teachers, Students, Homework and others).
  - Target database should be sqlite (filename main.db localted
   in current directory)
  - ORM framework should support migrations.

Utilizing that framework capabilities, create
a migration file, creating all necessary database structures.
a migration file (separate) creating at least one record in each
 created database table
(*) optional task: write standalone script (get_report.py)
 that retrieves and stores the following information into CSV file report.csv
for all done (completed) homeworks:
Student name (who completed homework) Creation date Teacher name
 who created homework
Utilize ORM capabilities as much as possible, avoiding
 executing raw SQL queries.
"""
import datetime

from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///sqlite3.db')


class DeadlineError(Exception):
    """Класс, наследуемый от Exception, реализует ошибку при истечении
    сроков выполнения домашнего задания
    """
    pass


class Homework(Base):
    __tablename__ = 'homeworks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    created = Column(DateTime(), default=datetime.datetime.now())
    deadline = Column(Integer, nullable=False)
    homeworkresults = relationship("HomeworkResult", backref='homework')


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    homeworkresults = relationship("HomeworkResult", backref='student')


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    homeworkresults = relationship("HomeworkResult", backref='teacher')


def is_active(homework):
    """Проверка срока задания
    :param homework: Домашняя работа, которую проверяем
    :return:True, если время выполнения не истекло, False иначе
    :rtype: bool
    """
    session = sessionmaker(bind=engine)
    session = session()
    flag = datetime.datetime.now() < \
        datetime.timedelta(days=homework.deadline) + homework.created
    session.close()
    return flag


class HomeworkResult(Base):
    __tablename__ = 'homeworkresults'
    id = Column(Integer, primary_key=True, autoincrement=True)
    solution = Column(String(100), nullable=False)
    created = Column(DateTime(), default=datetime.datetime.now())
    student_id = Column(Integer, ForeignKey('students.id'))
    homework_id = Column(Integer, ForeignKey('homeworks.id'))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))


def do_homework(student, homework: Homework, solution):
    """Метод, реализующий выполнение домашнего задания

    :param student: Студент, выполняющий домашнюю работу
    :param homework: Домашняя работа, которую выполняет студент
    :type homework: Homework
    :param solution: Решение домашней работы
    :type solution: str
    :raise DeadlineError: если домашняя работа просрочена
    :return: Выполненная домашняя работа, выполненная студентом
    или ничего если работа просрочена
    :rtype: HomeworkResult, None
        """
    if is_active(homework):
        return HomeworkResult(
            homework_id=homework.id,
            solution=solution,
            student_id=student.id
        )
    else:
        raise DeadlineError("You are late")


def create_homework(text, time):
    """Метод, реализующий создание домашнего задания

    :param text: текст задания
    :type text: str
    :param time: Время выполнения в днях
    :type time: int
    :return: Домашнее задание с параметрами text, time
    :rtype: Homework
    """
    return Homework(name=text, deadline=time)


def check_homework(homeworkresult):
    """Метод, реализующий проверку выполненного домашнего задания
    если домашнее задание выполненно правильно,
    добавляет его в выполненные
    :param homeworkresult: выполненное домашнее задание
    :type homeworkresult: HomeworkResult
    """
    session = sessionmaker(bind=engine)
    session = session()
    if len(homeworkresult.solution) > 5:
        results = session.query(HomeworkResult.solution)\
            .filter(HomeworkResult.homework_id ==
                    homeworkresult.homework_id).all()
        if homeworkresult.solution not in results:
            session.add(homeworkresult)
            session.commit()
            session.close()
            return True
    session.close()
    return False


def reset_results(homework: Homework = None):
    """Метод, реализующий очистку хранилища выполненных работ
    для работы homework или всего хранилища если вызывается без параметра
    :param homework: домашнее задание, defaults to None
    :type homework: Homework, None
    """
    session = sessionmaker(bind=engine)
    session = session()
    if homework is None:
        session.query(HomeworkResult).delete(synchronize_session='fetch')
        session.commit()
    else:
        session.query(HomeworkResult).filter(
            HomeworkResult.homework_id == homework.id
        ).delete(synchronize_session='fetch')
        session.commit()
    session.close()


Base.metadata.create_all(engine)
