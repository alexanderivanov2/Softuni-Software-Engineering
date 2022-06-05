rows, columns = [int(x) for x in input().split(", ")]

matrix = []
columns_sums = []

for row in range(rows):
    elements = [int(x) for x in input().split(" ")]
    matrix.append(elements)

for column_index in range(columns):
    current_row_sum = 0
    for rows_index in range(rows):
        current_row_sum += matrix[rows_index][column_index]
    columns_sums.append(current_row_sum)

[print(x) for x in columns_sums]
