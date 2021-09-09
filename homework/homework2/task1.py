"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
import unicodedata
from collections import Counter
from operator import itemgetter
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    temp_final = []
    with open(file_path) as fi:
        for line in fi:
            line = line.strip(string.punctuation).split(' ')
            for word in line:
                chars = Counter(word)
                if len(temp_final) < 10:
                    temp_final.append([word, len(word), len(chars)])
                    continue
                temp_final.sort(key=itemgetter(2, 1))
                if temp_final[0][2] < len(chars):
                    temp_final.pop(0)
                    temp_final.append([word, len(word), len(chars)])
                elif (temp_final[0][2] == len(chars) and
                        temp_final[0][1] < len(word)):
                    temp_final.pop(0)
                    temp_final.append([word, len(word), len(chars)])
    temp_final.sort(key=itemgetter(2, 1))
    final = []
    for j in temp_final:
        final.append(j[0])
    return final


def get_rarest_char(file_path: str) -> str:
    char = Counter()
    with open(file_path) as fi:
        for line in fi:
            char1 = Counter(line)
            char = char + char1
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
                if c not in string.printable:
                    amount += 1
    return amount


def get_most_common_non_ascii_char(file_path: str) -> str:
    char = Counter()
    with open(file_path) as fi:
        for line in fi:
            char1 = Counter(line)
            char = char + char1
    if len(char.most_common(1)) == 0:
        return "File is empty"
    for i in char.most_common():
        if i[0] not in string.printable:
            return i[0]
