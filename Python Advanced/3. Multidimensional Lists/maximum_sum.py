def create_matrix():
    rows_size, columns_size = [int(x) for x in input().split()]
    demo = []
    for create_row in range(rows_size):
        elements = [int(x) for x in input().split()]
        demo.append(elements)
    return demo, rows_size, columns_size


def calculate_3x3_sum(copy_matrix, row_index, column_index):
    current_3x3_sum = 0
    for row1 in range(row_index, row_index + 3):
        for column2 in range(column_index, column_index + 3):
            current_3x3_sum += copy_matrix[row1][column2]
    return current_3x3_sum


def finding_best_3x3_sum(matrix2, row_size2, column_size2):
    best_sum1 = 0
    best_row1 = 0
    best_column1 = 0
    for index_row in range(row_size2 - 2):
        for index_column in range(column_size2 - 2):
            current_sum = calculate_3x3_sum(matrix2, index_row, index_column)
            if current_sum > best_sum1:
                best_sum1 = current_sum
                best_row1 = index_row
                best_column1 = index_column
    return best_sum1, best_row1, best_column1


def print_results(matrix_result, sum_result, row_result, column_result):
    print(f"Sum = {sum_result}")
    for r in range(row_result, row_result + 3):
        for c in range(column_result, column_result + 3):
            print(matrix_result[r][c], end=" ")
        print()


matrix, row_size, column_size = create_matrix()
best_sum, best_row, best_column = finding_best_3x3_sum(matrix, row_size, column_size)
print_results(matrix, best_sum, best_row, best_column)
