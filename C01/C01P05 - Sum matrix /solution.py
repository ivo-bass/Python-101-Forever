def sum_matrix(matrix):
    # return sum(sum(matrix[row_i]) for row_i in range(len(matrix)))

    result = 0

    for row in matrix:
        for element in row:
            result += element

    return result


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_matrix(m) == 45)

m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(sum_matrix(m) == 0)

m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(sum_matrix(m) == 55)
