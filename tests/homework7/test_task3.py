import pytest

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


@pytest.mark.parametrize("test_input,expected",
                         [(row_x, "x wins!"), (column_o, "o wins!"),
                          (diagonal1_x, "x wins!"), (diagonal2_o, "o wins!"),
                          (draw, "draw!"), (unfinished, "unfinished!")])
def test_parametrized(test_input, expected):
    assert tic_tac_toe_checker(test_input) == expected

