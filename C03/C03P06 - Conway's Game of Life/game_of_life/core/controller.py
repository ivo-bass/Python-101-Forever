import os
import time
from copy import deepcopy

from numpy import array

from .helpers import stringify, count_live_neighbours, eval_cell_destiny


class Game:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.board = array([array([False for c in range(cols)]) for r in range(rows)])
        self.is_still = False
        self.generation = 0

    def set_alive(self, row_idx: int, col_idx: int):
        self.board[row_idx][col_idx] = True

    def show_board(self):
        os.system('clear')
        print("Generation: ", self.generation)
        for row in self.board:
            print(''.join(map(stringify, row)))
        time.sleep(0.1)

    def next_generation(self):
        self.is_still = True
        matrix = deepcopy(self.board)
        for r_idx, row in enumerate(matrix):
            for c_idx, value in enumerate(row):
                live_neighbours = count_live_neighbours(matrix, r_idx, c_idx)
                new_value = eval_cell_destiny(live_neighbours, value)
                if value != new_value:
                    self.board[r_idx][c_idx] = new_value
                    self.is_still = False
        self.generation += 1
