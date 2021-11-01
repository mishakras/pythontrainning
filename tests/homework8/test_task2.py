import os

from homework.homework8.task2 import TableData


def test_len():
    directory = os.path.dirname(os.path.abspath(__file__))
    table = TableData(directory + '/example.sqlite', 'presidents')
    assert len(table) == 3


def test_getter():
    directory = os.path.dirname(os.path.abspath(__file__))
    table = TableData(directory + '/example.sqlite', 'presidents')
    assert table['Yeltsin'] == ('Yeltsin', 999, 'Russia')


def test_contains():
    directory = os.path.dirname(os.path.abspath(__file__))
    table = TableData(directory + '/example.sqlite', 'presidents')
    assert 'Yeltsin' in table


def test_not_contains():
    directory = os.path.dirname(os.path.abspath(__file__))
    table = TableData(directory + '/example.sqlite', 'presidents')
    assert 'Misha' not in table


def test_iter():
    directory = os.path.dirname(os.path.abspath(__file__))
    table = TableData(directory + '/example.sqlite', 'presidents')
    for i in table:
        print(i)
    assert i == ('Big Man Tyrone', 101, 'Kekistan')
