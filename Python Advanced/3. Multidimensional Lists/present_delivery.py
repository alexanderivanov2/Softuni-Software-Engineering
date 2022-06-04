def create_matrix(n):
    demo_matrix = []
    a_coordinate = []
    nice_kids = 0
    for i in range(n):
        l = [el for el in input().split()]
        if "S" in l:
            a_coordinate = [i, l.index("S")]
        if "V" in l:
            nice_kids += l.count("V")
        demo_matrix.append(l)
    return demo_matrix, a_coordinate, nice_kids


presents_count = int(input())
rows = int(input())
columns = rows
matrix, santa, nice_kids = create_matrix(rows)
row = santa[0]
col = santa[1]
all_kids = nice_kids
command = input()
out_of_present = False

while not command == "Christmas morning" and presents_count > 0:
    if command == "up" and rows > row - 1 >= 0:
        matrix[row][col] = "-"
        row -= 1
    elif command == "down" and rows > row + 1 >= 0:
        matrix[row][col] = "-"
        row += 1
    elif command == "left" and columns > col - 1 >= 0:
        matrix[row][col] = "-"
        col -= 1
    elif command == "right" and columns > col + 1 >= 0:
        matrix[row][col] = "-"
        col += 1
    else:
        command = input()
        continue
    if matrix[row][col] == "V":
        nice_kids -= 1
        presents_count -= 1
        matrix[row][col] = "S"
    elif matrix[row][col] == "X":
        matrix[row][col] = "S"
    elif matrix[row][col] == "C":
        if row - 1 >= 0:
            if matrix[row - 1][col] == "V":
                nice_kids -= 1
                presents_count -= 1
            elif matrix[row - 1][col] == "X":
                presents_count -= 1
            matrix[row - 1][col] = "-"
        if row + 1 < rows:
            if matrix[row + 1][col] == "V":
                nice_kids -= 1
                presents_count -= 1
            elif matrix[row + 1][col] == "X":
                presents_count -= 1
            matrix[row + 1][col] = "-"
        if col + 1 < columns:
            if matrix[row][col + 1] == "V":
                nice_kids -= 1
                presents_count -= 1
            elif matrix[row][col + 1] == "X":
                presents_count -= 1
            matrix[row][col + 1] = "-"
        if col - 1 >= 0:
            if matrix[row][col - 1] == "V":
                nice_kids -= 1
                presents_count -= 1
            elif matrix[row][col - 1] == "X":
                presents_count -= 1
            matrix[row][col - 1] = "-"
    matrix[row][col] = "S"
    if presents_count == 0:
        out_of_present = True
        break
    command = input()

if out_of_present and nice_kids > 0:
    print("Santa ran out of presents!")

for l in matrix:
    print(" ".join(el for el in l))

if nice_kids == 0:
    print(f"Good job, Santa! {all_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
