def create_matrix(r):
    demo_matrix = []
    for i in range(r):
        row = [el for el in input().split()]
        demo_matrix.append(row)
    return demo_matrix


def calculate_squares(matrix, rows, columns):
    count = 0
    for r in range(rows - 1):
        for c in range(columns - 1):
            el = matrix[r][c]
            if matrix[r][c + 1] == el and el == matrix[r + 1][c] and el == matrix[r + 1][c + 1]:
                count += 1
    return count


rows, columns = [int(i) for i in input().split()]
matrix = create_matrix(rows)
squares = calculate_squares(matrix, rows, columns)
print(squares)
