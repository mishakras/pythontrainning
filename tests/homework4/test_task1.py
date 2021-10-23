import os

import pytest

from homework.homework4.task1 import read_magic_number


@pytest.fixture()
def create_good_file():
    f = open("good_file.txt", 'x')
    f.write('2')
    f.close()
    yield "good_file.txt"
    os.remove("good_file.txt")


@pytest.fixture()
def create_bad_file():
    f = open("bad_file.txt", 'x')
    f.write('10')
    f.close()
    yield "bad_file.txt"
    os.remove("bad_file.txt")


@pytest.fixture()
def create_exception_file():
    f = open("except_file.txt", 'x')
    f.write('jd')
    f.close()
    yield "except_file.txt"
    os.remove("except_file.txt")


def test_good(create_good_file):
    assert read_magic_number(create_good_file)


def test_bad(create_bad_file):
    assert not read_magic_number(create_bad_file)


def test_except(create_exception_file):
    with pytest.raises(ValueError, match="Error occured"):
        read_magic_number(create_exception_file)


def test_no_file():
    with pytest.raises(ValueError, match="Error occured"):
        read_magic_number("aaa")
