import random
import numpy as np

class Board():
    def __init__(self):
        self.board = [ ['b',1,2], [3,4,5], [6,7,8] ]

        self.f = self.g + self.h

    def randomize(self):
        for i in self.board:
            random.shuffle(i)
            for j in self.board:
                random.shuffle(j)
        return self.board
    def move(self):




def manhattanDistance():
    manhattan = 0
    for i in range(3):
        for j in range(3):
            if self.board[i][j] == 'b':
                continue
            else:
                current_board = current_board[i][j]
                current_values = [current_board//3, current_board%3]
                manhattan += manhattan_calculation([i,j],current_values)
    return manhattan

def manhattan_calculation(a,b):
    return abs(a[0] - b[0]) + abs(a[1]-b[1])
#This will return the difference between two points of the matrix

def idastar(board, heuristics):
    board.g = 0
    board.h = hueristics(board)
    board.f = board.g + board.h

    goal = [['b',1,2], [3,4,5], [6,7,8]]

    win_condition = False

    while win_condition == False:
        board.heuristics