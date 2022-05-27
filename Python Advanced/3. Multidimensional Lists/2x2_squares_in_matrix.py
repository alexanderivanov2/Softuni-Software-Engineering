def create_matrix():
    rows, columns = [int(x) for x in input().split()]
    demo_matrix = []
    for row in range(rows):
        elements = [x for x in input().split()]
        demo_matrix.append(elements)
    return demo_matrix, columns


def search_equal_cells(copy_matrix, column_len):
    count = 0
    for i_row in range(len(copy_matrix) - 1):
        for i_column in range(column_len - 1):
            if copy_matrix[i_row][i_column] == copy_matrix[i_row][i_column + 1] == copy_matrix[i_row + 1][i_column] == \
                    copy_matrix[i_row + 1][i_column + 1]:
                count += 1
    return count


matrix, column_size = create_matrix()
search_2x2 = search_equal_cells(matrix, column_size)
print(search_2x2)
