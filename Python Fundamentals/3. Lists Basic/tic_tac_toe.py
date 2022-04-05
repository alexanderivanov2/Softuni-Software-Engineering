def check_right_diagonal(matrix):
    if matrix[2][0] == matrix[1][1] == matrix[0][2] == 1:
        return 1
    elif matrix[2][0] == matrix[1][1] == matrix[0][2] == 2:
        return 2
    return 0


def check_left_diagonal(matrix):
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 1:
        return 1
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] == 2:
        return 2
    return 0


def check_rows(matrix):
    for row in range(3):
        if matrix[row][0] == matrix[row][1] == matrix[row][2] == 1:
            return 1
        elif matrix[row][0] == matrix[row][1] == matrix[row][2] == 2:
            return 2
    return 0


def check_col(matrix):
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] == 1:
            return 1
        elif matrix[0][col] == matrix[1][col] == matrix[2][col] == 2:
            return 2
    return 0


def print_result(result):
    if result == 1:
        print("First player won")
    elif result == 2:
        print("Second player won")
    else:
        print("Draw!")


matrix = [[int(el) for el in input().split()] for i in range(3)]
right_diagonal = check_right_diagonal(matrix)
left_diagonal = check_left_diagonal(matrix)
rows = check_rows(matrix)
columns = check_col(matrix)

result = right_diagonal + left_diagonal + columns + rows
print_result(result)
