from typing import List, Any
import copy
from piece import Piece
from constants import *

def create_hexagon(size) -> List[List[Any]]:
        '''creates inner hexagon of the board'''
        n = size + 1 #hexagon's side is 1 unit larger than triangle's
        hex = []
        #upper trapeziod
        for i in range(n, 2*n):
            sub = []
            for j in range(i):
                sub.append(None) 
            hex.append(sub)
        
        #bottom trapeziod
        for i in range(2*n - 2, n-1, -1):
            sub = []
            for j in range(i):
                sub.append(None)
            hex.append(sub)
        return hex
    
def create_triangle(size) -> List[List[Any]]:
    '''Equilateral triangle's sides are of length n and then
    attached to hex of size len 'n+1' '''
    n = size
    triangle = [[None] * i for i in range(1, n+1)]
    return triangle


def append_corner_triangles(hexagon, triangle) -> None:
    '''append 4 corner triangles to haxagon's horizontal sides'''
    # append upper corner triangles (inverted triangles)
    n = len(hexagon[0])
    inverted_triangle = triangle[::-1]
    copy_inverted = copy.deepcopy(inverted_triangle)
    cop = copy.deepcopy(triangle)
    for i in range(len(inverted_triangle)):
        hexagon[i] = inverted_triangle[i] + hexagon[i] + \
                    copy_inverted[i]
    
    #append bottom corner trinagles (upright ones)
    for i in range(len(triangle)):
        hexagon[n+i] = triangle[i] + hexagon[n+i] + cop[i]


def append_upper_bottom_hex(hexagon, triangle) -> List[List[Any]]:
    '''adds top and bottom triangles to the hexagon'''
    total = []
    total.extend(triangle)
    total.extend(hexagon)
    inverse = copy.deepcopy(triangle)[::-1]
    total.extend(inverse)
    return total



def fill_bottom_triangle(size, board):
    '''triangle number 1'''
    color = 1
    n = size
    for i in range(-1, -(n+1), -1):
        for j in range(len(board[i])):
            board[i][j] = Piece(color, (i, j), COLOR_LST[color-1])
            

def fill_top_triangle(size, board):
    color = 2
    n = size
    for i in range(n):
        for j in range(len(board[i])):
            board[i][j] = Piece(color, (i, j), COLOR_LST[color-1])
                

def fill_upper_left_triangle(size, board):
    '''triangle number 3'''
    color = 3
    n = size
    c = 0
    for i in range(n, 2*n):
        for j in range(n-c):
            board[i][j] = Piece(color, (i, j), COLOR_LST[color-1])
        c += 1

def fill_upper_right_triangle(size, board):
    '''triangle number 4'''
    color = 4
    n = size
    c = 0
    for i in range(n, 2*n):
        for j in range(2*n+1, 3*n+1-c):
            board[i][j] = Piece(color, (i, j), COLOR_LST[color-1])
        c += 1

def fill_bottom_right_triangle(size, board):
    '''triangle number 5'''
    color = 5
    n = size
    c = 0
    for i in range(-(n+1), -(2*n+1), -1):
        for j in range(-1, -n+c-1, -1):
            board[i][j] = Piece(color, (i, j), COLOR_LST[color-1])
        c += 1

def fill_bottom_left_triangle(size, board):
    '''triangle number 6'''
    color = 6
    n = size
    c = 0
    for i in range(-(n+1), -(2*n+1), -1):
        for j  in range(0, n - c):
            board[i][j] = Piece(color, (i, j), COLOR_LST[color-1])
        c += 1
