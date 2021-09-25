"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
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


def find_in_list_tuple_set(iterator, element: Any) -> int:
    temp = 0
    for value in iterator:
        if isinstance(value, dict):
            temp += find_occurrences(value, element)
        elif isinstance(value, list or set or tuple):
            temp += find_in_list_tuple_set(value, element)
        elif value == element:
            temp += 1
    return temp


def find_occurrences(tree: dict, element: Any) -> int:
    temp = 0
    for _, value in tree.items():
        if isinstance(value, dict):
            temp += find_occurrences(value, element)
        elif isinstance(value, list or set or tuple):
            temp += find_in_list_tuple_set(value, element)
        elif value == element:
            temp += 1
    return temp


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
