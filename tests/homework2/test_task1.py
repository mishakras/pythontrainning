from homework2.task1 import get_rarest_char, get_most_common_non_ascii_char, get_longest_diverse_words
from homework2.task1 import count_non_ascii_chars, count_punctuation_chars
import os


def test_rarest_char_positive():
    dir = os.path.dirname(os.path.abspath(__file__))
    dir = dir + "/task1.txt"
    assert get_rarest_char(dir) == '"'


def test_most_common_non_ascii_char_positive():
    dir = os.path.dirname(os.path.abspath(__file__))
    dir = dir + "/task1.txt"
    assert get_most_common_non_ascii_char(dir) == 'ы'


def test_longest_diverse_words_positive():
    dir = os.path.dirname(os.path.abspath(__file__))
    dir = dir + "/task1words.txt"
    assert get_longest_diverse_words(dir) == \
           ["asd", "asdf", "asdfg", "asdfgh", "asdfghj",
            "asdfghjkl", "agagaga", "kkkkkll", "bnmbnm", "uuuuuuuuyy"]


def test_count_non_ascii_chars_positive():
    dir = os.path.dirname(os.path.abspath(__file__))
    dir = dir + "/task1.txt"
    assert count_non_ascii_chars(dir) == 5


def test_count_punctuation_chars_positive():
    dir = os.path.dirname(os.path.abspath(__file__))
    dir = dir + "/task1.txt"
    assert count_punctuation_chars(dir) == 9
