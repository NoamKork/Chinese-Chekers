import pygame
import numpy as np
from typing import Tuple

# canvas resolution
WIDTH, HEIGHT = 600, 600

# rgb
Color = Tuple[int, int, int]
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)

COLOR_DICT = {
    "R": (255, 0, 0),
    "G": (0, 255, 0),
    "B": (0, 0, 255),
    "O":  (255, 165, 0),
    "Y": (255, 255, 0),
    "P": (160, 32, 240)
}

COLOR_LST = ['R', 'B', 'G', 'Y', 'O', 'P']

GREY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


#unit vectors according to new X and Y plane
X_UNIT = np.array([1,0])
Y_UNIT = np.array([1,1])

Coordinates = Tuple[int, int]



