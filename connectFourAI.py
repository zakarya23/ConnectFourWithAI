import numpy as np
import random 
import pygame 
import sys 
import math 

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROWS = 6 
COLUMNS = 7 

PLAYER = 0 
ROBOT = 1

EMPTY = 0 
PLAYER_PIECE = 1 
ROBOT_PIECE = 2

LEN_WINDOW = 4 

def create_board(): 
    board = np.zeroes((ROWS, COLUMNS))
    return board

def piece_drop(board, row, column, piece): 
    board[row][column] = piece

def is_valid_location(board, column): 
    return board[ROWS - 1][COLUMNS] == 0 



