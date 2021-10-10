from homework.homework8.task1 import KeyValueStorage


def test_one_key(tmpdir):
    tmpdir.join('task1.txt').write('key=value')
    storage = KeyValueStorage(str(tmpdir)+'/task1.txt')
    assert storage['key'] == 'value'


def test_some_keys(tmpdir):
    tmpdir.join('task1.txt').write('key=value\nkey2=value2\nkey3=value3')
    storage = KeyValueStorage(str(tmpdir)+'/task1.txt')
    assert storage['key2'] == 'value2'


def test_one_attribute(tmpdir):
    tmpdir.join('task1.txt').write('key=value')
    storage = KeyValueStorage(str(tmpdir)+'/task1.txt')
    assert storage.key == 'value'


def test_some_attributes(tmpdir):
    tmpdir.join('task1.txt').write('key=value\nkey2=value2\nkey3=value3')
    storage = KeyValueStorage(str(tmpdir)+'/task1.txt')
    assert storage.key2 == 'value2'


def test_attribute_replace(tmpdir):
    tmpdir.join('task1.txt').write('key=value\nkey=value2\nkey3=value3')
    storage = KeyValueStorage(str(tmpdir)+'/task1.txt')
    print(storage.__dir__())
    assert storage.key == 'value'
