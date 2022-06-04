def create_matrix(r):
    demo_matrix = []
    for i in range(r):
        row = [int(el) for el in input().split()]
        demo_matrix.append(row)
    return demo_matrix


def find_max_start_index(matrix, rows, columns):
    start_row = 0
    start_col = 0
    maximum_sum = 0
    for r in range(rows - 2):
        for c in range(columns - 2):
            current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2]
            current_sum += matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2]
            current_sum += matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
            if current_sum > maximum_sum:
                start_row = r
                start_col = c
                maximum_sum = current_sum
    print(f"Sum = {maximum_sum}")
    return start_row, start_col


rows, columns = [int(i) for i in input().split()]
matrix = create_matrix(rows)
row, col = find_max_start_index(matrix, rows, columns)
for r in range(row, row+3):
    for c in range(col, col +3):
        print(matrix[r][c], end=" ")
    print()