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


def delete_backspace(first: str) -> str:
    temp1 = 0
    temp3 = 0
    for index, char in enumerate(first):
        if char == '#':
            temp3 += 1
            if index == len(first) - 1:
                first = first[:temp1 - temp3 + 1]
        elif temp3 == 0:
            temp1 = index
        elif temp3 > 0:
            if temp1 > temp3 - 1:
                first = first[:temp1 - temp3 + 1] + first[index:]
            else:
                first = first[index:]
            return first
    return first


def backspace_compare(first: str, second: str):
    temp1 = 0
    for index, char in enumerate(first):
        if char == '#':
            temp1 += 1
        else:
            first = first[temp1:]
            break
    while first.find('#') > -1:
        first = delete_backspace(first)
    temp1 = 0
    for index, char in enumerate(second):
        if char == '#':
            temp1 += 1
        else:
            second = second[temp1:]
            break
    while second.find('#') > -1:
        second = delete_backspace(second)
    return first == second


if __name__ == '__main__':
    print(backspace_compare('a##c', '#a#c'))
