from homework2.task1 import get_rarest_char, get_most_common_non_ascii_char, get_longest_diverse_words
from homework2.task1 import count_non_ascii_chars, count_punctuation_chars


def test_rarest_char_positive():
    assert get_rarest_char("tests/homework2/task1.txt") == '"'


def test_most_common_non_ascii_char_positive():
    assert get_most_common_non_ascii_char("tests/homework2/task1.txt") == 'ы'


def test_longest_diverse_words_positive():
    assert get_longest_diverse_words("tests/homework2/task1.txt")


def test_count_non_ascii_chars_positive():
    assert count_non_ascii_chars("tests/homework2/task1.txt") == 5


def test_count_punctuation_chars_positive():
    assert count_punctuation_chars("tests/homework2/task1.txt") == 9
