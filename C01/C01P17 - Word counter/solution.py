PRIMARy_DIAGONAL = (1, 1)


def count_word_in_text(text, word):
    return text.count(word) + text[::-1].count(word)


def is_valid_index(matrix, x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def search_horizontals(matrix, word):
    count = 0
    for row in matrix:
        row_text = ''.join(row)
        count += count_word_in_text(row_text, word)
    return count


def search_verticals(matrix, word):
    count = 0
    for col_i in range(len(matrix[0])):
        col_text = ''
        for row_i in range(len(matrix)):
            col_text += matrix[row_i][col_i]
        count += count_word_in_text(col_text, word)
    return count


def search_primary_diagonals(matrix, word):
    count = 0
    first_row = 0
    diagonal_text = ''
    for col_i in range(len(matrix[0]) - len(word), -1, -1):
        while is_valid_index(matrix, first_row, col_i):
            diagonal_text += matrix[first_row][col_i]
            first_row += 1
            col_i += 1
        count += count_word_in_text(diagonal_text, word)
        first_row = 0
        diagonal_text = ''
    first_col = 0
    for row_i in range(1, len(matrix) - len(word) + 1):
        while is_valid_index(matrix, row_i, first_col):
            diagonal_text += matrix[row_i][first_col]
            row_i += 1
            first_col += 1
        count += count_word_in_text(diagonal_text, word)
        first_col = 0
        diagonal_text = ''
    return count


def search_secondary_diagonals(matrix, word):
    count = 0
    first_row = 0
    diagonal_text = ''
    for col_i in range(len(word)-1, len(matrix[0])):
        while is_valid_index(matrix, first_row, col_i):
            diagonal_text += matrix[first_row][col_i]
            first_row += 1
            col_i += -1
        count += count_word_in_text(diagonal_text, word)
        first_row = 0
        diagonal_text = ''
    first_col = 0
    for row_i in range(1, len(matrix) - len(word) + 1):
        while is_valid_index(matrix, row_i, first_col):
            diagonal_text += matrix[row_i][first_col]
            row_i += 1
            first_col += -1
        count += count_word_in_text(diagonal_text, word)
        first_col = 0
        diagonal_text = ''
    return count


def check_for_palindrome(word, count):
    if word == word[::-1]:
        count //= 2
    return count


def word_counter(matrix, word):
    count = 0
    count += search_horizontals(matrix, word)
    count += search_verticals(matrix, word)
    count += search_primary_diagonals(matrix, word)
    count += search_secondary_diagonals(matrix, word)
    count = check_for_palindrome(word, count)
    return count


word = "ivan"
matrix = [
    ["i", "v", "a", "n"],
    ["e", "v", "n", "h"],
    ["i", "n", "a", "v"],
    ["m", "v", "v", "n"],
    ["q", "r", "i", "t"]
]
print(word_counter(matrix, word))

word = "actually"
matrix = [
    ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],
    ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],
    ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],
    ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],
    ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],
    ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],
    ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]
]
print(word_counter(matrix, word))

word = "madam"
matrix = [
    ["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"],
    ["e", "v", "m", "h", "t", "r", "x", "e", "k", "y", "m", "a"],
    ["i", "a", "c", "a", "u", "a", "l", "l", "y", "a", "c", "x"],
    ["m", "v", "c", "n", "d", "u", "a", "m", "d", "t", "l", "u"],
    ["q", "t", "i", "t", "w", "a", "a", "a", "u", "p", "r", "x"],
    ["p", "e", "m", "a", "d", "a", "m", "l", "l", "y", "w", "p"],
    ["o", "y", "h", "t", "e", "e", "l", "u", "f", "p", "q", "n"],
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e"]
]
print(word_counter(matrix, word))


word = "python"
matrix = [
  ["r", "u", "b", "y"],
  ["r", "u", "b", "y"],
  ["r", "u", "b", "y"],
  ["r", "u", "b", "y"],
]
print(word_counter(matrix, word))
