"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import math
import string
import unicodedata
from typing import List
from collections import Counter


def get_longest_diverse_words(file_path: str) -> List[str]:
    temp_final = []
    with open(file_path) as fi:
        for line in fi:
            line = line.strip(string.punctuation).split(' ')
            for word in line:
                chars = Counter()
                for char in word:
                    chars[char] += 1
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
    char = Counter()
    with open(file_path) as fi:
        for line in fi:
            for c in line:
                char[c] += 1
    chars = Counter()
    chars.subtract(char)
    min_char = chars.most_common(1)[0][0]
    if len(chars.most_common(1)) == 0:
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
    chars = Counter()
    with open(file_path) as fi:
        for line in fi:
            for c in line:
                if c not in string.printable:
                    chars[c] += 1
    max_char = chars.most_common(1)[0][0]
    if len(chars.most_common(1)) == 0:
        return "File is empty"
    return max_char
