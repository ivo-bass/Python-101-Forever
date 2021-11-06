from dataclasses import dataclass

from numpy import array
from .cell import Cell


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.matrix = self.__create_matrix()

    def __create_matrix(self):
        return array([array([Cell(r_i, c_i, False) for c_i in range(self.width)]) for r_i in range(self.height)])
