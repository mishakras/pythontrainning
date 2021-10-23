from pathlib import Path

from homework.homework9.task3 import universal_file_counter


def test_without_tokens_one_file(tmpdir):
    tmpdir.join('test31.txt').write('1\n2\n3\n4\n')
    path = Path(str(tmpdir))
    assert universal_file_counter(path, 'txt') == 4


def test_without_tokens_some_file(tmpdir):
    tmpdir.join('test31.txt').write('1\n2\n3\n4\n')
    tmpdir.join('test32.txt').write('1\n2\n3\n4\n')
    tmpdir.join('test33.txt').write('1\n2\n3\n4\n')
    path = Path(str(tmpdir))
    assert universal_file_counter(path, 'txt') == 12


def test_with_tokens_one_file(tmpdir):
    tmpdir.join('test31.txt').write('1 2 3 4')
    path = Path(str(tmpdir))
    assert universal_file_counter(path, 'txt', str.split) == 4


def test_with_tokens_some_file(tmpdir):
    tmpdir.join('test31.txt').write('1 2 3 4')
    tmpdir.join('test32.txt').write('1\n2\n3\n4\n')
    tmpdir.join('test33.txt').write('1 2 34')
    path = Path(str(tmpdir))
    assert universal_file_counter(path, 'txt', str.split) == 11
