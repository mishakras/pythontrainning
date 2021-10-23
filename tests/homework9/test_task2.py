import pytest

from homework.homework9.task2 import Suppressor, suppressor


def test_suppressor_class():
    with Suppressor(IndexError):
        [][2]


def test_suppressor_function():
    with suppressor(IndexError):
        [][2]


def test_negative_suppressor_function():
    with suppressor(TypeError):
        with pytest.raises(IndexError):
                [][2]


def test_negative_suppressor_class():
    with Suppressor(TypeError):
        with pytest.raises(IndexError):
                [][2]
