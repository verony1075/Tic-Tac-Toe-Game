##############                              qq1`-qqqe########################################################
# Authors: Jalin Jones
# Username: jjjonesj
#
# Assignment: P01
# Purpose:  Test the Kwasiada game
######################################################################e

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import kwasiada_frankaa as kf
from kwasiada_frankaa import Board
import sys

from inspect import getframeinfo, stack


def returnWinner(Board):
    for row in Board:
        if len(set(row)) == 1:
            return row[0]
    return -1
def checkRows(Board):
    for row in Board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(Board):
    if len(set([Board[i][i] for i in range(len(Board))])) == 1:
        return Board[0][0]
    if len(set([Board[i][len(Board)-i-1] for i in range(len(Board))])) == 1:
        return Board[0][len(Board)-1]
    return 0

def checkRowWin(Board):
    for b in [Board]:
        result = checkRows(b)
        if result == "O":
            result = "O Wins - PASS"
            return result
        elif result == "X":
            result = "X Wins - PASS"
            return result
        else:
            result = "FAIL"
            return result
def checkDiagonalWin(Board):
    for b in [Board]:
        result = checkDiagonals(b)
        if result == "O":
            result = "O Wins - PASS"
            return result
        elif result == "X":
            result = "X Wins - PASS"
            return result
        else:
            result = "FAIL"
            return result

b1 = [['X', 'O', 'X'],
     ['O', 'X', 'O'],
     ['O', 'X', 'O']]

b2 = [['O', 'X', 'X'],
     ['O', 'O', 'O'],
     ['X', 'o', 'X']]

b3 = [['X', 'O', 'X'],
     ['O', 'X', 'O'],
     ['O', 'X', 'X']]

b4 = [['X', 'O', 'O'],
     ['X', 'X', 'X'],
     ['O', 'X', 'O']]

print("Testing Row Wins")
print(checkRowWin(b1))
print(checkRowWin(b2))
print(checkRowWin(b3))
print(checkRowWin(b4))

print("Testing Diagonal Wins")
print(checkDiagonalWin(b1))
print(checkDiagonalWin(b2))
print(checkDiagonalWin(b3))
print(checkDiagonalWin(b4))