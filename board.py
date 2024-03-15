from typing import List, Any
import tkinter as tk
from constants import *

class Board:
    def __init__(self, size, num_players) -> None:
        if not isinstance(size, int) or (not 0 <= size <= 10):
            raise ValueError("Size must be between 0 to 10")
        if not isinstance(num_players, int) or not 2 <= num_players <= 6:
            raise ValueError("Number of players must be between 2 to 6")
        
        self.__size = size #why doesn't work with __size????
        self.__board = self.__create_board()
        self.__selected_piece = None
        self.__num_players = num_players
        self.__num_pieces = num_players * ((self.size / 2) * (self.size + 1))
        
    @property
    def size(self):
        return self.__size #same ????    
    
    @property
    def board(self):
        return self.__board
    
    def __create_board(self):
        ...

    def __create_hexa(self):
        m = self.size
        matrix_hexa_up = [[0 for i in range(j+m)] for j in range(m)]
        matrix_hexa_up_will_be_down = [[0 for i in range(j+m)] for j in range(m)]
        return matrix_hexa_up + matrix_hexa_up_will_be_down[::-1]
        


board = Board(2,4)
org = board.board



    
    

            