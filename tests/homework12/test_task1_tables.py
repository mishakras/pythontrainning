import homework.homework12.task1_tables

metadata = homework.homework12.task1_tables.Base.metadata


def test_homeworks():
    for i in metadata.sorted_tables:
        if 'homeworks' == i.name:
            return
    assert False


def test_teachers():
    for i in metadata.sorted_tables:
        if 'teachers' == i.name:
            return
    assert False


def test_students():
    for i in metadata.sorted_tables:
        if 'students' == i.name:
            return
    assert False


def test_homeworkresults():
    for i in metadata.sorted_tables:
        if 'homeworkresults' == i.name:
            if len(i.columns) == 6:
                return
    assert False


def test_homeworks_columns():
    for i in metadata.sorted_tables:
        if 'homeworks' == i.name:
            if len(i.columns) == 4:
                return
    assert False


def test_teachers_columns():
    for i in metadata.sorted_tables:
        if 'teachers' == i.name:
            if len(i.columns) == 3:
                return
    assert False


def test_students_columns():
    for i in metadata.sorted_tables:
        if 'students' == i.name:
            if len(i.columns) == 3:
                return
    assert False


def test_homeworkresults_columns():
    for i in metadata.sorted_tables:
        if 'homeworkresults' == i.name:
            if len(i.columns) == 6:
                return
    assert False
