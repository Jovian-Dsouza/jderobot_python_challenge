#!/usr/bin/env python3

import unittest
from gameOfLife import Board

class TestGOFBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(6,6, random_init=False)

    def test_countNeighbour0(self):
        self.assertEqual(self.board._countNeighbour(1,1) , 0)
    
    def test_countNeighbour1(self):
        for x in range(-1, 2): #-1 , 0, 1
            for y in range(-1, 2): #-1 , 0 , 1
                if not (x == 0 and y == 0):
                    n_i = 1 + x
                    n_j = 1 + y
                    self.board._board[n_i][n_j].setAlive()
                    self.assertEqual(self.board._countNeighbour(1,1) , 1)
                    self.board._board[n_i][n_j].setDead()
    
    def _add_live_neighbours(self, neighbour_count):
        if neighbour_count == 0:
            return

        count = 0
        for x in range(-1, 2): #-1 , 0, 1
            for y in range(-1, 2): #-1 , 0 , 1
                if (not (x == 0 and y == 0)):
                    n_i = 1 + x
                    n_j = 1 + y

                    if(count == neighbour_count):
                        return
                    
                    self.board._board[n_i][n_j].setAlive()
                    count = count + 1

        
    def test_update_alive_0_neighbours_dies(self):
        '''Any live cell with less than 2 neighbour dies'''
        self.board._board[1][1].setAlive()

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_alive_1_neighbours_dies(self):
        '''Any live cell with less than 2 neighbour dies'''
        self.board._board[1][1].setAlive()
        self._add_live_neighbours(1)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_alive_2_neighbours_lives(self):
        '''Any live cell with two or three live neighbours lives'''
        self.board._board[1][1].setAlive()
        self._add_live_neighbours(2)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), True)
    
    def test_update_alive_3_neighbours_lives(self):
        '''Any live cell with two or three live neighbours lives'''
        self.board._board[1][1].setAlive()
        self._add_live_neighbours(3)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), True)
    
    def test_update_alive_4_neighbours_dies(self):
        '''Any live cell with more than three live neighbours dies'''
        self.board._board[1][1].setAlive()

        self._add_live_neighbours(4)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)

    def test_update_alive_5_neighbours_dies(self):
        '''Any live cell with more than three live neighbours dies'''
        self.board._board[1][1].setAlive()
        self._add_live_neighbours(5)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_alive_6_neighbours_dies(self):
        '''Any live cell with more than three live neighbours dies'''
        self.board._board[1][1].setAlive()
        self._add_live_neighbours(6)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_alive_7_neighbours_dies(self):
        '''Any live cell with more than three live neighbours dies'''
        self.board._board[1][1].setAlive()
        self._add_live_neighbours(7)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_alive_8_neighbours_dies(self):
        '''Any live cell with more than three live neighbours dies'''
        self.board._board[1][1].setAlive()
        self._add_live_neighbours(8)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_dead_0_neighbours_dies(self):
        '''Any dead cell with not exactly three live neighbours remains dead'''
        self.board._board[1][1].setDead()

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_dead_1_neighbours_dies(self):
        ''''Any dead cell with not exactly three live neighbours remains dead'''
        self.board._board[1][1].setDead()
        self._add_live_neighbours(1)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_dead_2_neighbours_lives(self):
        '''Any dead cell with not exactly three live neighbours remains dead'''
        self.board._board[1][1].setDead()
        self._add_live_neighbours(2)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_dead_3_neighbours_lives(self):
        '''Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.'''
        self.board._board[1][1].setDead()
        self._add_live_neighbours(3)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), True)
    
    def test_update_dead_4_neighbours_dies(self):
        '''Any dead cell with not exactly three live neighbours remains dead'''
        self.board._board[1][1].setDead()

        self._add_live_neighbours(4)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)

    def test_update_dead_5_neighbours_dies(self):
        '''Any dead cell with not exactly three live neighbours remains dead'''
        self.board._board[1][1].setDead()
        self._add_live_neighbours(5)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_dead_6_neighbours_dies(self):
        '''Any dead cell with not exactly three live neighbours remains dead'''
        self.board._board[1][1].setDead()
        self._add_live_neighbours(6)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_dead_7_neighbours_dies(self):
        '''Any dead cell with not exactly three live neighbours remains dead'''
        self.board._board[1][1].setDead()
        self._add_live_neighbours(7)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)
    
    def test_update_dead_8_neighbours_dies(self):
        '''Any dead cell with not exactly three live neighbours remains dead'''
        self.board._board[1][1].setDead()
        self._add_live_neighbours(8)

        self.board.updateBoard()

        self.assertEqual(self.board._board[1][1].isAlive(), False)

    #Test for static shapes
    def _set_predefined_shape(self, shape):
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if (shape[i][j] == 1):
                    self.board._board[i][j].setAlive()
                else:
                    self.board._board[i][j].setDead()
    
    def _check_predefined_shape(self, shape):
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if (shape[i][j] == 1):
                    self.assertEqual(self.board._board[i][j].isAlive(), True)
                else:
                    self.assertEqual(self.board._board[i][j].isAlive(), False)
   
    def test_box_shape(self):
        shape = [[1,1],
                [1,1]]
        
        self._set_predefined_shape(shape)
        self.board.updateBoard()
        self._check_predefined_shape(shape)
    
    def test_beehive_shape(self):
        shape = [[0, 1, 1, 0],
                [1, 0, 0, 1],
                [0, 1, 1, 0]]
        
        self._set_predefined_shape(shape)
        self.board.updateBoard()
        self._check_predefined_shape(shape)
    
    def test_loaf_shape(self):
        shape = [[0, 1, 1, 0],
                 [1, 0, 0, 1],
                 [0, 1, 0, 1],
                 [0, 0, 1, 0]]
        
        self._set_predefined_shape(shape)
        self.board.updateBoard()
        self._check_predefined_shape(shape)
    
    def test_boat_shape(self):
        shape = [[1, 1, 0],
                 [1, 0, 1],
                 [0, 1, 0]]
        
        self._set_predefined_shape(shape)
        self.board.updateBoard()
        self._check_predefined_shape(shape)
    
    def test_tub_shape(self):
        shape = [[0, 1, 0],
                 [1, 0, 1],
                 [0, 1, 0]]
        
        self._set_predefined_shape(shape)
        self.board.updateBoard()
        self._check_predefined_shape(shape)

    def test_blinker_period2(self):
        shape = [[0, 0, 0],
                 [1, 1, 1],
                 [0, 0, 0]]
        period = 2
    
        self._set_predefined_shape(shape)

        for i in range(period):
            self.board.updateBoard()
    
        self._check_predefined_shape(shape)

    
if __name__ == "__main__":
    unittest.main()

    
