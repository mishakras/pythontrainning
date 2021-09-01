import os

from homework2.task1 import count_non_ascii_chars, count_punctuation_chars, \
    get_longest_diverse_words, get_most_common_non_ascii_char, get_rarest_char


def test_rarest_char_positive():
    directory = os.path.dirname(os.path.abspath(__file__))
    directory = directory + "/task1.txt"
    assert get_rarest_char(directory) == '"'


def test_most_common_non_ascii_char_positive():
    directory = os.path.dirname(os.path.abspath(__file__))
    directory = directory + "/task1.txt"
    assert get_most_common_non_ascii_char(directory) == 'ы'


def test_longest_diverse_words_positive():
    directory = os.path.dirname(os.path.abspath(__file__))
    directory = directory + "/task1words.txt"
    assert get_longest_diverse_words(directory) == \
           ["asd", "asdf", "asdfg", "asdfgh", "asdfghj",
            "asdfghjkl", "agagaga", "kkkkkll", "bnmbnm", "uuuuuuuuyy"]


def test_count_non_ascii_chars_positive():
    directory = os.path.dirname(os.path.abspath(__file__))
    directory = directory + "/task1.txt"
    assert count_non_ascii_chars(directory) == 5


def test_count_punctuation_chars_positive():
    directory = os.path.dirname(os.path.abspath(__file__))
    directory = directory + "/task1.txt"
    assert count_punctuation_chars(directory) == 9
