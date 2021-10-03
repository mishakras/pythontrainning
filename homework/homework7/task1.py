"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
import re


def replacer(match):
    return match[0][0]


def backspace_compare(first: str, second: str):
    while first.find('#') > -1:
        if first.find('#') == 0:
            first = first[1:]
            continue
        if first.find('#') == 1:
            first = first[2:]
            continue
        first = re.sub(r'..#', replacer, first)
    while second.find('#') > -1:
        if second.find('#') == 0:
            second = second[1:]
            continue
        if second.find('#') == 1:
            second = second[2:]
            continue
        second = re.sub(r'..#', replacer, second)
    return first == second


if __name__ == '__main__':
    print(backspace_compare('a##c', '#a#c'))
