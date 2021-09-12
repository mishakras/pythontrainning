import sys
from contextlib import redirect_stdout
import io
import pytest
from homework.homework4.task3 import my_precious_logger


def test_stdout():
    f = io.StringIO()
    with redirect_stdout(f):
        my_precious_logger("abcdef")
    assert f.getvalue() == 'abcdef'


def test_stderr():
    backup = sys.stderr
    sys.stderr = io.StringIO()
    my_precious_logger("error:abcdef")
    temp = sys.stderr.getvalue()
    sys.stderr.close()
    sys.stderr = backup
    assert temp == "error:abcdef"
