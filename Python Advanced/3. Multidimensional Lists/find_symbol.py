def create_matrix(n):
    project_matrix = []
    for row in range(n):
        elements = [x for x in input()]
        project_matrix.append(elements)
    return project_matrix


def found_char(copy_matrix, search_char_copy):
    for row_index in range(len(copy_matrix)):
        for column_index in range(len(copy_matrix[row_index])):
            if copy_matrix[row_index][column_index] == search_char_copy:
                return f"({row_index}, {column_index})"


size = int(input())
matrix = create_matrix(size)
search_chr = input()
searching = found_char(matrix, search_chr)

if searching:
    print(searching)
else:
    print(f"{search_chr} does not occur in the matrix")