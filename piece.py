from constants import *
from typing import Tuple, List, Dict

class Piece:
    def __init__(self, player_num: int, location: Coordinates, color: str) -> None:
        self.__player_num = player_num
        self.__location = location
        self.__color = (color, COLOR_DICT[color])
        self.__selected = False
        self.__mouse_hovering = False
    
    def get_player_num(self):
        return self.__player_num
    
    def get_color(self):
        return self.__color[0]
    
    def get_location(self) -> Coordinates:
        return self.__location
    
    def set_location(self, new_loc: Coordinates):
        self.__location = new_loc
    
      
        
    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements 
                 permitted by this piece.
        """
        moves_dict: Dict[str, np.ndarray] = {}
        moves_dict['u'] = np.asarray(self.__location) + Y_UNIT
        moves_dict['d'] = np.asarray(self.__location) - Y_UNIT
        moves_dict['r'] = np.asarray(self.__location) + X_UNIT
        moves_dict['l'] = np.asarray(self.__location) - X_UNIT
        moves_dict['ul'] = np.asarray(self.__location) + (Y_UNIT - X_UNIT)
        moves_dict['dr'] = np.asarray(self.__location) + (-Y_UNIT + X_UNIT)
        
        return moves_dict
        
