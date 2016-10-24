from unicurses import *

stdscr = initscr() # initializes the standard screen
addstr('Hello World!\n')
getch()