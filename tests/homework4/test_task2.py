import pytest
from mock import MagicMock, patch

from homework.homework4.task2 import count_dots_on_i


def test_good_some_i():
    with patch('urllib.request.urlopen') as MockClass:
        cm = MagicMock()
        cm.read.return_value = 'aaiiia'
        MockClass.return_value = cm
        assert count_dots_on_i("iii") == 3


def test_good_no_i():
    with patch('urllib.request.urlopen') as MockClass:
        cm = MagicMock()
        cm.read.return_value = 'abcdef'
        MockClass.return_value = cm
        assert count_dots_on_i("iii") == 0


def test_raised_error():
    with pytest.raises(ValueError,
                       match="Unreachable "
                             "https://docs.python.org/3/library/urllib."):
        count_dots_on_i("https://docs.python.org/3/library/urllib.")
