#!/usr/bin/env python3

from gameOfLife import Board
import curses
import time
import json

class CursesBoard(Board):
    def __init__(self, scr, rows, cols, random_init=True):
        self.stdscr = scr
        self.stdscr.clear()

        #Get window size and give padding 
        Y, X = self.stdscr.getmaxyx()
        max_X, max_Y = X-2, Y-2-2

        if(cols > max_X) or (rows > max_Y):
            if cols > max_X:
                cols = max_X
            if rows > max_Y:
                rows = max_Y
            self.stdscr.addstr(max_Y+2, 0 , "Board size cant fit in window , Size change to (%d x %d)" % (rows, cols))

        center_X = max_X // 2
        center_Y = max_Y // 2

        self.start_X = center_X - cols // 2
        self.start_Y = center_Y - rows // 2

        super().__init__(rows, cols, random_init)

    def display_board(self):
        """Display the board"""
        for i in range(0, self._cols):
            for j in range(0, self._rows):
                if self._board[j][i].isAlive():
                    self.stdscr.addch(self.start_Y+j+1, self.start_X+i+1, '*')
                else:
                    self.stdscr.addch(self.start_Y+j+1, self.start_X+i+1, ' ')
        self.stdscr.refresh()
    
    def draw_border(self):
        """Draw a border around the board"""
        border_line = '+'+(self._cols*'-')+'+'
        self.stdscr.addstr(self.start_Y, self.start_X, border_line)
        self.stdscr.addstr(self.start_Y + self._rows+1, self.start_X, border_line)
        for y in range(1, self._rows+1):
            self.stdscr.addstr(self.start_Y + y, self.start_X, '|')
            self.stdscr.addstr(self.start_Y + y, self.start_X + self._cols+1, '|')
        self.stdscr.refresh()

class App:
    def __init__(self, rows, cols, refresh_freq=10.0):
        self.rows , self.cols = rows, cols
        self.refresh_time = 1.0 / refresh_freq 
        curses.wrapper(self.main)
    
    def erase_menu(self):
        self.stdscr.move(self.menu_y, 0)
        self.stdscr.clrtoeol()
        self.stdscr.move(self.menu_y+1, 0)
        self.stdscr.clrtoeol()
        self.stdscr.refresh()

    def display_menu(self):
        "Display the menu commands"
        self.erase_menu()
        self.stdscr.addstr(self.menu_y, 4,
                    "CONWAYS GAME OF LIFE - a cellular automaton")
        self.stdscr.addstr(self.menu_y+1, 4,
                    '(R)andom fill (S)tep once (C)ontinuously (E)rase (Q)uit')
        self.stdscr.refresh()

    def main(self, stdscr):
        self.stdscr = stdscr

        #Clear Screen
        self.stdscr.clear()
        self.stdscr_y, self.stdscr_x = self.stdscr.getmaxyx()

        # display the menu of keys
        self.menu_y = (self.stdscr_y-3)+1
        self.display_menu()
        
        # Allocate a subwindow for the board 
        subwin = self.stdscr.subwin(self.stdscr_y-3, self.stdscr_x, 0, 0)
        self.board = CursesBoard(subwin, self.rows, self.cols, True)
        self.board.draw_border()
        self.board.display_board()

        self.keyloop() 
        
    def keyloop(self):
        while (True):
            c = self.stdscr.getch()             
            if not (0 < c <256):
                break
            c = chr(c)

            if c in 'Rr': #Random Fill
                self.board._randomInitialize()
                self.board.display_board()
            
            elif c in 'Ss': #Step Once
                self.board.updateBoard()
                self.board.display_board()

            elif c in 'Cc': #Continously update
                self.erase_menu()
                self.stdscr.addstr(self.menu_y, 6, ' Hit any key to stop continuously updating the screen.')
                self.stdscr.refresh()

                self.stdscr.nodelay(1) #Dont wait for keystroke
                while (True):
                    #Exit if any key is pressed
                    c = self.stdscr.getch()
                    if c != -1:
                        break

                    #Update and display board
                    self.board.updateBoard()
                    self.board.display_board()
                    time.sleep(self.refresh_time) #Wait for some time to see the animations

                self.stdscr.nodelay(0)      
                self.display_menu()

            elif c in 'Ee': #Erase
                self.board.erase()
                self.board.display_board()

            elif c in 'Qq': #Quit
                break

            
if __name__ == '__main__':

    with open('config.json') as file:
        data = json.load(file)

    app = App(data['height'] , data['width'], data['refresh_freq'])

