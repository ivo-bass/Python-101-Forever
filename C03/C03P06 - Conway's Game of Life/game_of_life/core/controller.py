import os
import time
from copy import deepcopy

from numpy import array

DELTAS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
)


class Controller:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.board = array([array([False for c in range(cols)]) for r in range(rows)])
        self.is_still = False
        self.generation = 0

    @staticmethod
    def __stringify(value: bool):
        return '\u2588' * 2 if value else "\u2591" * 2

    @staticmethod
    def __eval_cell_destiny(live_neighbours, value):
        if not value and live_neighbours == 3:
            return True
        if value and not 2 <= live_neighbours <= 3:
            return False
        else:
            return value

    @staticmethod
    def __is_valid_cell(matrix, row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

    def __count_live_neighbours(self, matrix, r_idx, c_idx):
        count = 0
        for dx, dy in DELTAS:
            row, col = r_idx + dx, c_idx + dy
            if not self.__is_valid_cell(matrix, row, col):
                continue
            if matrix[row][col]:
                count += 1
        return count

    def set_alive(self, row_idx: int, col_idx: int):
        self.board[row_idx][col_idx] = True

    def set_glider(self, r_i, c_i):
        self.set_alive(r_i + 2, c_i)
        self.set_alive(r_i + 2, c_i + 1)
        self.set_alive(r_i + 2, c_i + 2)
        self.set_alive(r_i + 1, c_i + 2)
        self.set_alive(r_i, c_i + 1)

    def set_blinker(self, r_i, c_i):
        self.set_alive(r_i, c_i)
        self.set_alive(r_i, c_i + 1)
        self.set_alive(r_i, c_i + 2)

    def show_board(self):
        os.system('clear')
        print("Generation: ", self.generation)
        for row in self.board:
            print(''.join(map(self.__stringify, row)))
        time.sleep(0.1)

    def next_generation(self):
        self.is_still = True
        matrix = deepcopy(self.board)
        for r_idx, row in enumerate(matrix):
            for c_idx, value in enumerate(row):
                live_neighbours = self.__count_live_neighbours(matrix, r_idx, c_idx)
                new_value = self.__eval_cell_destiny(live_neighbours, value)
                if value != new_value:
                    self.board[r_idx][c_idx] = new_value
                    self.is_still = False
        self.generation += 1
