"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import math
import unicodedata
import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    temp_final = []
    with open(file_path) as fi:
        for line in fi:
            for i in string.punctuation:
                line = line.replace(i, ' ')
            line = line.split(' ')
            for word in line:
                chars = []
                for char in word:
                    if chars.count(char) == 0:
                        chars.append(char)
                if len(temp_final) < 10:
                    temp_final.append([word, len(chars)])
                    continue
                temp_final.sort()
                temp1 = -1
                temp2 = -1
                temp3 = math.inf
                temp4 = math.inf
                for index, j in enumerate(temp_final):
                    if len(j[0]) < temp3:
                        temp3 = len(j[0])
                        temp1 = index
                    if j[1] < temp4:
                        temp4 = j[1]
                        temp2 = index
                if len(chars) > temp4 and len(word) >= temp3:
                    temp_final.pop(temp2)
                    temp_final.append([word, len(chars)])
                    continue
                if len(word) > temp3 and len(chars) >= temp4:
                    temp_final.pop(temp1)
                    temp_final.append([word, len(chars)])
                    continue
    final = []
    for j in temp_final:
        final.append(j[0])
    return final


def get_rarest_char(file_path: str) -> str:
    char_amount = []
    chars = []
    min_char_amount = math.inf
    with open(file_path) as fi:
        for line in fi:
            for c in line:
                flag = True
                if chars.count(c) > 0:
                    char_amount[chars.index(c)] += 1
                    flag = False
                if flag:
                    char_amount.append(1)
                    chars.append(c)
    for index, i in enumerate(chars):
        if char_amount[index] < min_char_amount:
            min_char = i
            min_char_amount = char_amount[index]
    if min_char_amount == math.inf:
        return "File is empty"
    return min_char


def count_punctuation_chars(file_path: str) -> int:
    amount = 0
    with open(file_path) as fi:
        for line in fi:
            for c in line:
                if unicodedata.category(c)[0] == 'P':
                    amount += 1
    return amount


def count_non_ascii_chars(file_path: str) -> int:
    amount = 0
    with open(file_path) as fi:
        for line in fi:
            for c in line:
                if ord(c) > 127:
                    amount += 1
    return amount


def get_most_common_non_ascii_char(file_path: str) -> str:
    char_amount = []
    chars = []
    max_char_amount = 0
    with open(file_path) as fi:
        for line in fi:
            for c in line:
                if ord(c) > 127:
                    flag = True
                    if chars.count(c) > 0:
                        char_amount[chars.index(c)] += 1
                        flag = False
                    if flag:
                        char_amount.append(1)
                        chars.append(c)
    for index, i in enumerate(chars):
        if char_amount[index] > max_char_amount:
            max_char = i
            max_char_amount = char_amount[index]
    if max_char_amount == 0:
        return "File is empty"
    return max_char
