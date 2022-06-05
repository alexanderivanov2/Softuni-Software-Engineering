def create_matrix(n):
    demo = []
    for row in range(n):
        elements = [int(x) for x in input().split(", ")]
        demo.append(elements)
    return demo


def calculate_biggest_square(matrix2, cut_rows, cut_columns):
    square_up = []
    square_down = []
    total_square = []
    total_square_sum = 0
    for row in range(cut_rows):
        for column in range(cut_columns):
            square_up.append(matrix2[row][column])
            square_up.append(matrix2[row][column + 1])
            square_down.append(matrix2[row + 1][column])
            square_down.append(matrix2[row + 1][column + 1])
            square_size = sum(square_up) + sum(square_down)
            if total_square_sum < square_size:
                total_square = [square_up, square_down]
                total_square_sum = sum([sum(total_square[x]) for x in range(len(total_square))])
            square_up = []
            square_down = []
    return total_square


rows, columns = [int(x) for x in input().split(", ")]
matrix = create_matrix(rows)
rows2 = rows - 1
columns2 = columns - 1
biggest_square = calculate_biggest_square(matrix, rows2, columns2)

for square_part in biggest_square:
    [print(x, end=" ") for x in square_part]
    print()
print(sum([sum(biggest_square[x]) for x in range(len(biggest_square))]))
