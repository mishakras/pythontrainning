import pytest

from homework.homework6.task2 import\
    Teacher, Student, HomeworkResult, DeadlineError


def test_student_do_homework_late():
    h = Teacher.create_homework("test", 0)
    s = Student("Misha", "Kras")
    with pytest.raises(DeadlineError, match="You are late"):
        s.do_homework(h, "s")


def test_not_homework_for_homeworkresult():
    with pytest.raises(TypeError, match="That is not homework"):
        HomeworkResult('s', 's', 's')


def test_check_of_homework():
    opp_teacher = Teacher('Daniil', 'Shadrin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(
        docs_hw, 'I have done this hw too')
    result_2 = lazy_student.do_homework(docs_hw, 'done')

    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)

    assert len(Teacher.homework_done[docs_hw]) == 1


def test_check_of_homework_different_teachers():
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    good_student = Student('Lev', 'Sokolov')

    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(
        docs_hw, 'I have done this hw too')

    opp_teacher.check_homework(result_1)
    advanced_python_teacher.check_homework(result_1)

    assert len(Teacher.homework_done[docs_hw]) == 2


def test_reset_results():
    opp_teacher = Teacher('Daniil', 'Shadrin')

    good_student = Student('Lev', 'Sokolov')

    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(
        docs_hw, 'I have done this hw too')

    opp_teacher.check_homework(result_1)
    opp_teacher.reset_results(docs_hw)
    assert len(Teacher.homework_done[docs_hw]) == 0


def test_reset_results_all():
    opp_teacher = Teacher('Daniil', 'Shadrin')

    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(
        docs_hw, 'I have done this hw too')

    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)
    opp_teacher.reset_results()
    assert len(Teacher.homework_done[docs_hw]) == 0
