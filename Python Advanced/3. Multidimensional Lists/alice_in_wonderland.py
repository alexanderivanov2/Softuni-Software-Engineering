def create_matrix(n):
    demo_matrix = []
    a_coordinate = []
    for i in range(n):
        l = input().split()
        if "A" in l:
            a_coordinate = [i, l.index("A")]
        demo_matrix.append(l)
    return demo_matrix, a_coordinate


rows = int(input())
matrix, alice = create_matrix(rows)
columns = len(matrix[0])
tea = 0
c_row = alice[0]
c_col = alice[1]
stop = False
while tea < 10 and not stop:
    direction = input()
    if direction == "left":
        matrix[c_row][c_col] = "*"
        if rows > c_row >= 0 and columns > c_col - 1 >= 0:
            c_col -= 1
            if matrix[c_row][c_col] == "R":
                stop = True
            elif not matrix[c_row][c_col] == "." and not matrix[c_row][c_col] == "*":
                tea += int(matrix[c_row][c_col])
        else:
            stop = True
    elif direction == "right":
        matrix[c_row][c_col] = "*"
        if rows > c_row >= 0 and columns > c_col + 1 >= 0:
            c_col += 1
            if matrix[c_row][c_col] == "R":
                stop = True
            elif not matrix[c_row][c_col] == "." and not matrix[c_row][c_col] == "*":
                tea += int(matrix[c_row][c_col])
        else:
            stop = True
    elif direction == "up":
        matrix[c_row][c_col] = "*"
        if rows > c_row - 1 >= 0 and columns > c_col >= 0:
            c_row -= 1
            if matrix[c_row][c_col] == "R":
                stop = True
            elif not matrix[c_row][c_col] == "." and not matrix[c_row][c_col] == "*":
                tea += int(matrix[c_row][c_col])
        else:
            stop = True
    elif direction == "down":
        matrix[c_row][c_col] = "*"
        if rows > c_row + 1 >= 0 and columns > c_col >= 0:
            c_row += 1
            if matrix[c_row][c_col] == "R":
                stop = True
            elif not matrix[c_row][c_col] == "." and not matrix[c_row][c_col] == "*":
                tea += int(matrix[c_row][c_col])
        else:
            stop = True
    matrix[c_row][c_col] = "*"

if stop:
    print("Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")

for l in matrix:
    print(" ".join(l))
