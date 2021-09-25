from homework.homework7.task2 import find_occurrences


easy_tree = {
    "first": "RED",
    "second": "valued",
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
        }
     },
    "fourth": "RED",
}


complex_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", ["of", "RED", "valued"]],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def test_easy():
    assert find_occurrences(easy_tree, "BLUE") == 1


def test_complicated():
    assert find_occurrences(complex_tree, "RED") == 6


def test_nothing():
    assert find_occurrences(complex_tree, "abcdwr") == 0
