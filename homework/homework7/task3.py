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
from typing import List

import numpy


def tic_tac_toe_checker(board: List[List]) -> str:
    for row in board:
        if row[0] == "x" and row[1] == "x" and row[2] == "x":
            return "x wins!"
        if row[0] == "o" and row[1] == "o" and row[2] == "o":
            return "o wins!"
    for one, two, three in zip(board[0], board[1], board[2]):
        if one == "x" and two == "x" and three == "x":
            return "x wins!"
        if one == "o" and two == "o" and three == "o":
            return "o wins!"
    if board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x":
        return "x wins!"
    if board[2][0] == "x" and board[1][1] == "x" and board[0][2] == "x":
        return "x wins!"
    if board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o":
        return "o wins!"
    if board[2][0] == "o" and board[1][1] == "o" and board[0][2] == "o":
        return "o wins!"
    for row in board:
        for letter in row:
            if letter == "-":
                return "unfinished!"
    return "draw!"
