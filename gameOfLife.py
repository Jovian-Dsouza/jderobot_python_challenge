#!/usr/bin/env python3

'''
Game of Life
'''

from random import randint
from copy import deepcopy

class Cell:
    def __init__(self, state=False):
        self._alive = state
    
    def isAlive(self):
        return self._alive

    def setDead(self):
        self._alive = False
    
    def setAlive(self):
        self._alive = True
    
class Board:
    def __init__(self, rows, cols, random_init=True):
        self._rows = rows
        self._cols = cols

        self._board = [[Cell() for j in range(cols)] for i in range(rows)]

        if random_init:
            self._randomInitialize()
    
    def _randomInitialize(self):
        for row in self._board:
            for cell in row:
                #33% chance that cell is alive
                if randint(0, 2) == 1:
                    cell.setAlive()
                else:
                    cell.setDead()
    
    def erase(self):
        for row in self._board:
            for cell in row:
                cell.setDead()

    def _isValid(self, i, j):
        return (0 <= i and i < self._rows and 0 <= j and j < self._cols)

    def _countNeighbour(self, i, j):
        '''
        Returns the number of alive neighbour of a cell (i, j)
        '''
        count = 0

        for x in range(-1, 2): #-1 , 0, 1
            for y in range(-1, 2): #-1 , 0 , 1
                if not (x == 0 and y == 0):
                    n_i = i + x
                    n_j = j + y

                    if self._isValid(n_i, n_j):
                        if self._board[n_i][n_j].isAlive():
                            count = count + 1

        return count

    def updateBoard(self):
        new_board = deepcopy(self._board)

        for i in range(self._rows):
            for j in range(self._cols):
                neighbour_count = self._countNeighbour(i, j)

                isCurrentCellAlive = self._board[i][j].isAlive()

                if (isCurrentCellAlive):
                    if neighbour_count < 2 or neighbour_count > 3:
                        #Cell dies : Underpopulation or Overpopulation
                        new_board[i][j].setDead()
                    
                else:
                    if neighbour_count == 3:
                        #Cell Alive : Reproduction
                        new_board[i][j].setAlive() 

        self._board = deepcopy(new_board)

                

if __name__ == "__main__":
    board = Board(10 , 10)

    user_action = ''
    while user_action != 'q':
        user_action = input('Press enter to add generation or q to quit:')

        if user_action == '':
            board.drawInTerminal()
            board.updateBoard()