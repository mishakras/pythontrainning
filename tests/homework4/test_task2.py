import urllib.request
import unittest
from mock import patch, MagicMock

from homework.homework4.task2 import count_dots_on_i


@patch('urllib.request.urlopen')
def pathing_urlopen_good(self, mock_urlopen):
    cm = MagicMock()
    cm.getcode.return_value = 200
    cm.read.return_value = 'iii'
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm


@patch('urllib.request.urlopen')
def pathing_urlopen_except(self, mock_urlopen):
    cm = MagicMock()
    cm.getcode.return_value = 404
    cm.read.return_value = 'iii'
    mock_urlopen.return_value = cm


def test_good():
    temp = MagicMock()
    temp.getcode.return_value = 200
    temp.read.return_value = 'iii'
    with patch('urllib.request.urlopen', return_value=temp):
        assert count_dots_on_i("iii") == 3



