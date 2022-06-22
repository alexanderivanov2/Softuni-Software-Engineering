def find_near_bombs_last_col(matrix, row, col):
    number = 0
    if not row == 0:
        if matrix[row - 1][col] == "*":
            number += 1
        if matrix[row - 1][col - 1] == "*":
            number += 1
    if matrix[row][col - 1] == "*":
        number += 1
    if not row == len(matrix) - 1:
        if matrix[row + 1][col - 1] == "*":
            number += 1
        if matrix[row + 1][col] == "*":
            number += 1
    return number


def find_near_bombs_first_col(matrix, row, col):
    number = 0
    if not row == 0:
        if matrix[row - 1][col] == "*":
            number += 1
        if matrix[row - 1][col + 1] == "*":
            number += 1
    if matrix[row][col + 1] == "*":
        number += 1
    if not row == len(matrix) - 1:
        if matrix[row + 1][col + 1] == "*":
            number += 1
        if matrix[row + 1][col] == "*":
            number += 1
    return number


def find_near_bombs(matrix, row, col):
    number = 0
    if not row == 0:
        if matrix[row - 1][col] == "*":
            number += 1
        if matrix[row - 1][col - 1] == "*":
            number += 1
        if matrix[row - 1][col + 1] == "*":
            number += 1
    if matrix[row][col - 1] == "*":
        number += 1
    if matrix[row][col + 1] == "*":
        number += 1
    if not row == len(matrix) - 1:
        if matrix[row + 1][col - 1] == "*":
            number += 1
        if matrix[row + 1][col + 1] == "*":
            number += 1
        if matrix[row + 1][col] == "*":
            number += 1
    return number


n = int(input())
matrix = [[0 for i in range(n)] for row in range(n)]
bombs_num = int(input())

for i in range(bombs_num):
    r, c = input()[1:-1].split(', ')
    matrix[int(r)][int(c)] = "*"

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "*":
            continue
        if col == 0:
            number = find_near_bombs_first_col(matrix, row, col)
            matrix[row][col] = number
        elif col == n - 1:
            number = find_near_bombs_last_col(matrix, row, col)
            matrix[row][col] = number
        else:
            number = find_near_bombs(matrix, row, col)
            matrix[row][col] = number

for row in matrix:
    print(" ".join(str(el) for el in row))
