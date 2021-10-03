"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
import numpy
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    board = numpy.array(board)
    for row, _ in enumerate(board):
        flagx = True
        flago = True
        for item in board[row, :]:
            flagx = (flagx and item == 'x')
            flago = (flago and item == 'o')
        if flagx:
            return "x wins!"
        if flago:
            return "o wins!"
        flagx = True
        flago = True
        for item in board[:, row]:
            flagx = (flagx and item == 'x')
            flago = (flago and item == 'o')
        if flagx:
            return "x wins!"
        if flago:
            return "o wins!"
    flagx = True
    flago = True
    for row, _ in enumerate(board):
        flagx = (flagx and board[row, row] == 'x')
        flago = (flagx and board[row, row] == 'o')
    if flagx:
        return "x wins!"
    if flago:
        return "o wins!"
    flagx = True
    flago = True
    for row, _ in enumerate(board):
        flagx = (flagx and board[len(board)-row-1, row] == 'x')
        flago = (flago and board[len(board)-row-1, row] == 'o')
    if flagx:
        return "x wins!"
    if flago:
        return "o wins!"
    for row in board:
        for letter in row:
            if letter == "-":
                return "unfinished!"
    return "draw!"
