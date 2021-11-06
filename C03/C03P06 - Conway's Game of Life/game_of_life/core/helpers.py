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


def stringify(value: bool):
    return '\u2588' * 2 if value else "\u2591" * 2


def eval_cell_destiny(live_neighbours, value):
    if not value and live_neighbours == 3:
        return True
    if value and not 2 <= live_neighbours <= 3:
        return False
    else:
        return value


def is_valid_cell(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def count_live_neighbours(matrix, r_idx, c_idx):
    count = 0
    for dx, dy in DELTAS:
        row, col = r_idx + dx, c_idx + dy
        if not is_valid_cell(matrix, row, col):
            continue
        if matrix[row][col]:
            count += 1
    return count