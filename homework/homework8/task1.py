"""
We have a file that works as key-value storage, each line is represented as
 key and value separated by = symbol, example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers.
 If a value can be treated both as a number and a string,
  it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt') that has its keys and values
 accessible as collection items and as attributes. Example: storage['name']
  # will be string 'kek' storage.song_name # will be 'shadilay'
   storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when
 there's a line 1=something)
ValueError should be raised. File size is expected to be small,
 you are permitted to read it entirely into memory.
"""
import keyword
from unicodedata import category as cat


class KeyValueStorage:
    def __init__(self, file):
        self.storage = {}
        with open(file) as fi:
            for line in fi:
                line = line.split('=')
                key, value = line[0], line[1]
                try:
                    value = int(value)
                except Exception:
                    if value[len(value) - 1] == '\n':
                        value = value[:len(value) - 1]
                if key in keyword.kwlist or (cat(key[0])[0] != 'L'
                                             and cat(key[0]) != 'Nl'
                                             and key[0] != '_'):
                    raise ValueError("Wrong name for attribute")
                else:
                    self.storage[key] = value
                    if key not in self.__dir__():
                        setattr(KeyValueStorage, key, value)

    def __getitem__(self, item):
        return self.storage[item]

    def __setitem__(self, key, value):
        self.storage[key] = value
