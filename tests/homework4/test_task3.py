from homework.homework4.task3 import my_precious_logger


def test_stdout(capsys):
    my_precious_logger('abcdef')
    temp = capsys.readouterr()
    assert temp.out == 'abcdef'


def test_stderr(capsys):
    my_precious_logger('error:abcdef')
    temp = capsys.readouterr()
    assert temp.err == "error:abcdef"
