DELTAS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
)


def is_valid_index(index, matrix):
    return 0 <= index < len(matrix)


def sum_matrix(m):
    return sum(sum(row) for row in m)


def bomb_neighbours(matrix, x, y):
    value = matrix[x][y]
    for delta_x, delta_y in DELTAS:
        row_index = x + delta_x
        col_index = y + delta_y
        if not is_valid_index(row_index, matrix) or not is_valid_index(col_index, matrix):
            continue
        current_value = matrix[row_index][col_index]
        matrix[row_index][col_index] = current_value - value if current_value >= value else 0


def matrix_bombing_plan(matrix):
    result_dict = {}
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix_copy = [row.copy() for row in matrix]
            bomb_neighbours(matrix_copy, r, c)
            result_dict[(r, c)] = sum_matrix(matrix_copy)
    return result_dict
