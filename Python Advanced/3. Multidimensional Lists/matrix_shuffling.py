def create_matrix():
    get_rows, get_columns = [int(x) for x in input().split()]
    demo = []
    for get_row in range(get_rows):
        elements = input().split()
        demo.append(elements)
    return demo, get_rows, get_columns


matrix, rows, columns = create_matrix()
command = input()

while command != "END":
    if "swap" in command and len(command.split()) == 5:
        row1, col1, row2, col2 = [int(x) for x in command.split()[1:]]
        if row1 <= rows >= row2 and col1 <= columns >= col2:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for r in range(rows):
                print(' '.join(str(x) for x in matrix[r]))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input()
