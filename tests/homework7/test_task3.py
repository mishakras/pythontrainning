from homework.homework7.task3 import tic_tac_toe_checker

row_x = [["x", "x", "x"],
         ["-", "o", "o"],
         ["x", "o", "o"]]
column_o = [["o", "x", "o"],
            ["o", "o", "x"],
            ["o", "x", "x"]]
diagonal1_x = [["x", "o", "x"],
               ["o", "x", "o"],
               ["o", "x", "x"]]
diagonal2_o = [["x", "x", "o"],
               ["x", "o", "o"],
               ["o", "x", "x"]]
draw = [["x", "o", "x"],
        ["x", "o", "x"],
        ["o", "x", "o"]]
unfinished = [["-", "o", "x"],
              ["-", "-", "x"],
              ["o", "x", "o"]]


def test_row_x():
    assert tic_tac_toe_checker(row_x) == "x wins!"


def test_column_o():
    assert tic_tac_toe_checker(column_o) == "o wins!"


def test_diagonal1_x():
    assert tic_tac_toe_checker(diagonal1_x) == "x wins!"


def test_diagonal2_o():
    assert tic_tac_toe_checker(diagonal2_o) == "o wins!"


def test_unfinished():
    assert tic_tac_toe_checker(unfinished) == "unfinished!"


def test_draw():
    assert tic_tac_toe_checker(draw) == "draw!"
