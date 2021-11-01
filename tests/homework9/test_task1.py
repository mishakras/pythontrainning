from homework.homework9.task1 import merge_sorted_files


def test_one_file(tmpdir):
    tmpdir.join('test11.txt').write('1\n2\n3\n4\n')
    numbers = []
    for i in merge_sorted_files([str(tmpdir)+'/test11.txt']):
        numbers.append(i)
    assert numbers == [1, 2, 3, 4]


def test_some_file(tmpdir):
    tmpdir.join('test11.txt').write('1\n3\n')
    tmpdir.join('test12.txt').write('2\n4\n')
    tmpdir.join('test13.txt').write('6\n9\n')
    numbers = []
    for i in merge_sorted_files([str(tmpdir)+'/test11.txt',
                                 str(tmpdir)+'/test12.txt',
                                 str(tmpdir)+'/test13.txt']):
        numbers.append(i)
    assert numbers == [1, 2, 3, 4, 6, 9]
