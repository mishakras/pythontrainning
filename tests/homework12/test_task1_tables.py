import homework.homework12.task1_tables

metadata = homework.homework12.task1_tables.Base.metadata


def test_homeworks():
    flag = False
    for i in metadata.sorted_tables:
        if 'homeworks' == i.name:
            flag = True
    assert flag


def test_teachers():
    flag = False
    for i in metadata.sorted_tables:
        if 'teachers' == i.name:
            flag = True
    assert flag


def test_students():
    flag = False
    for i in metadata.sorted_tables:
        if 'students' == i.name:
            flag = True
    assert flag


def test_homeworkresults():
    flag = False
    for i in metadata.sorted_tables:
        if 'homeworkresults' == i.name:
            if len(i.columns) == 6:
                flag = True
    assert flag


def test_homeworks_columns():
    flag = False
    for i in metadata.sorted_tables:
        if 'homeworks' == i.name:
            if len(i.columns) == 4:
                flag = True
    assert flag


def test_teachers_columns():
    flag = False
    for i in metadata.sorted_tables:
        if 'teachers' == i.name:
            if len(i.columns) == 3:
                flag = True
    assert flag


def test_students_columns():
    flag = False
    for i in metadata.sorted_tables:
        if 'students' == i.name:
            if len(i.columns) == 3:
                flag = True
    assert flag


def test_homeworkresults_columns():
    flag = False
    for i in metadata.sorted_tables:
        if 'homeworkresults' == i.name:
            if len(i.columns) == 6:
                flag = True
    assert flag
