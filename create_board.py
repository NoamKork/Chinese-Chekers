###################
# implementation of the game board
# First make traditional, then try dynamic size
###############
from typing import List, Any
import tkinter as tk
from constants import *
from create_board_helper import *


class CreateBoard:
    '''Initializes a playing board'''
    
    def __init__(self, size, num_players) -> None:
        #check input
        if not isinstance(size, int) or (not 1 <= size <= 10):
            raise ValueError("Board size can be between 1 to 10")
        if not isinstance(num_players, int) or not 2 <= num_players <= 6 or num_players == 5:
            raise ValueError("Number of players can be 2, 3, 4 or 6")
        
        self.__size = size 
        self.__selected_piece = None
        self.__num_players = num_players
        self.__num_pieces = num_players * ((self.size / 2) * (self.size + 1))
        self.__board = self.__create_board()
        self.__populate()
        
        
    @property
    def size(self) -> int:
        return self.__size    

    
    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string representing the current status of the board.
        """
        board_str: str = ''
        board = self.__board
        n = self.size
        distance_from_edge = n + 1
        whitespaces = 3*n + 1 - 1
        width = (2 * distance_from_edge) + (3*n + 1) + whitespaces
        for i in range(len(board)):
            row = CreateBoard.add_spaces(CreateBoard.convert_to_str(board[i]))
            board_str += row.center(width, ' ')
            if i != len(board) - 1:
                board_str += '\n'
                
        return board_str         
    
    @staticmethod
    def add_spaces(row):
        return ' '.join(row)

    @staticmethod
    def convert_to_str(lst) -> str:
        str_lst = ''
        for i in range(len(lst)):
            if not lst[i]:
                str_lst += '.' # temporary. change later based on data in lst[i]
            else:
                str_lst += str(lst[i].get_color())
        return str_lst
    
    
    def __create_board(self):
        '''create a chess board of size n'''
        hexagon = create_hexagon(self.size) #central hexagon
        upright_triangle = create_triangle(self.size) 
        append_corner_triangles(hexagon, upright_triangle)
        new_triangle = create_triangle(self.size)
        total = append_upper_bottom_hex(hexagon, new_triangle)
        return total
    
    
    def __populate(self):
        '''fills the games board with players' respective pieces'''
        key_words = {"size": self.size, "board": self.__board}
        
        fill_funcs = {
        2: [fill_top_triangle, fill_bottom_triangle],
        3: [fill_bottom_triangle, fill_upper_left_triangle, fill_upper_right_triangle],
        4: [fill_top_triangle, fill_bottom_triangle, fill_upper_left_triangle,\
            fill_bottom_right_triangle],
        6: [fill_top_triangle, fill_bottom_triangle, fill_upper_left_triangle,\
            fill_upper_right_triangle, fill_bottom_right_triangle, fill_bottom_left_triangle]
    }

        for func in fill_funcs.get(self.__num_players, []):
            func(**key_words)
    
    
    def cell_list(self) -> List[Coordinates]:
        """
        This function returns the coordinates of cells in this board.
        :return: list of coordinates.
        """
        cell_list: List[Coordinates] = []
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                cell_list.append((i,j))
        return cell_list
    
    
    


        

    
board = CreateBoard(1, 2) 
    
print(board)  
print(board.cell_list())
    
    

        

        
    


# def f(n):
#     '''reference'''
#     for k in range(4*n+1):x=abs(k-2*n);y=2*n-x;p,q,r=" BP G..R YO "[(k-~k)//(n-~n)::4];print(" "*y,*p*x+q*-~y+r*x)
 

# print(f(-1))




