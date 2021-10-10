
"""
Write a function that merges integer from sorted files
 and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from typing import List


def gen_from_file(path):
    with open(path) as fi:
        for line in fi:
            yield int(line)


def merge_sorted_files(file_list: List):

    class Numbers:
        def __init__(self):
            files = []
            self.numbers = []
            for i in file_list:
                files.append(gen_from_file(i))
            current_numbers = []
            for i in files:
                current_numbers.append(next(i))
            while True:
                try:
                    min_value = min(filter(lambda x: x is not None,
                                           current_numbers))
                    self.numbers.append(min_value)
                    min_index = current_numbers.index(min_value)
                    try:
                        current_numbers[min_index] = next(files[min_index])
                    except StopIteration:
                        current_numbers[min_index] = None
                except ValueError:
                    break
            self.cursor = -1

        def __iter__(self):
            return iter(self.numbers)

    return Numbers()
