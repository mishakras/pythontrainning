"""
Write a function that takes directory path,
 a file extension and an optional tokenizer.
It will count lines in all files with that extension
 if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
"""
from pathlib import Path
from typing import Callable, Optional


def gen_from_file(path):
    with open(path) as fi:
        for line in fi:
            yield line


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    counter = 0
    for i in list(dir_path.glob('*.'+file_extension)):
        if not tokenizer:
            for line in gen_from_file(i):
                counter += 1
        else:
            for line in gen_from_file(i):
                counter += len(tokenizer(line))
    return counter
