
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


class Numbers:
    def __init__(self, file_list):
        self.files = [gen_from_file(file) for file in file_list]
        self.current_numbers = [next(gen) for gen in self.files]

    def __next__(self):
        try:
            min_value = min(filter(lambda x: x is not None,
                                   self.current_numbers))
            min_index = self.current_numbers.index(min_value)
            try:
                self.current_numbers[min_index] = next(self.files[min_index])
            except StopIteration:
                self.current_numbers[min_index] = None
            return min_value
        except ValueError:
            raise StopIteration

    def __iter__(self):
        return self


def merge_sorted_files(file_list: List):
    return Numbers(file_list)
