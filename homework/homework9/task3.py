"""
Write a function that takes directory path,
 a file extension and an optional tokenizer.
It will count lines in all files with that extension
 if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
"""
import os
from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Optional


@contextmanager
def cd_gen(path):
    cwd = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(cwd)


def gen_from_file(path):
    with open(path) as fi:
        for line in fi:
            yield line


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    dir_path = str(dir_path)
    with cd_gen(dir_path):
        temp = 0
        files = os.listdir(path=".")
        for i in files:
            if i.find("."+file_extension) != -1:
                if tokenizer is None:
                    for j in gen_from_file(i):
                        temp += 1
                else:
                    for j in gen_from_file(i):
                        temp += len(tokenizer(j))
        return temp
