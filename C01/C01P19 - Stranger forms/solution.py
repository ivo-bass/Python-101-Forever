TAKEN_SEAT = "*"
DIRECTIONS = {
    "A": (-1, 0),  # Above
    "R": (0, 1),   # Right
    "L": (0, -1),  # Left
    "B": (1, 0),   # Below
}


def get_cinema_layout(cinema_layout):
    # list of strings -> nested list
    return [list(line) for line in cinema_layout]


def get_friends_relative_positions(friends_configuration):
    # create dict and add center name's position
    center_friend = friends_configuration.pop(0)
    dd = {center_friend: (0, 0)}
    for config in friends_configuration:
        name_to_write, direction, name_to_check = config
        # sum the elements of tuples: (delta_x + previous_x, delta_y + previous_y)
        # and write the position for the given name related to the center name
        zip_direction_to_position = zip(DIRECTIONS[direction], dd.get(name_to_check))
        calc_position = map(sum, zip_direction_to_position)
        dd[name_to_write] = tuple(calc_position)
    return dd


def is_invalid_position(mat, r, c):
    max_r = len(mat) - 1
    max_c = len(mat[0]) - 1
    return any((r > max_r, c > max_c, r < 0, c < 0))


def place_names_in_matrix(cinema, deltas, row, col):
    new_layout = get_cinema_layout(cinema)
    # iterate through friends relative positions
    for name, (delta_r, delta_c) in deltas.items():
        # calculate new coordinates
        new_r = row + delta_r
        new_c = col + delta_c
        if is_invalid_position(cinema, new_r, new_c):
            return
        if new_layout[new_r][new_c] == TAKEN_SEAT:
            return
        # place name at position if it is valid
        new_layout[new_r][new_c] = name
    # if the iterations are completed this is valid formation
    return new_layout


def stranger_forms(cinema_layout, friends_configuration):
    possible = []
    friends_deltas = get_friends_relative_positions(friends_configuration)

    for row_index, row in enumerate(cinema_layout):
        for col_index, element in enumerate(row):

            if element == TAKEN_SEAT:
                continue

            new_layout = place_names_in_matrix(cinema_layout, friends_deltas, row_index, col_index)

            if new_layout is not None:
                # convert list back to string and append the valid formation to the result
                new_layout = ["".join(r) for r in new_layout]
                possible.append(new_layout)

    return possible


# ____TEST____
test_cinema_layout = [
    '..*...*.**',
    '.....**...',
    '*.*...*..*',
    '.**....*.*',
    '...*..*.*.',
    '.***...*..',
    '*......*.*',
    '.....**..*',
    '..*.*.*..*',
    '***.*.**..',
]
test_friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]
possible_configurations = stranger_forms(test_cinema_layout, test_friends_configuration)

for configuration in possible_configurations:
    for line in configuration:
        print(line)
    print()
