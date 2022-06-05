def create_matrix(n):
    demo_matrix = []
    a_coordinate = []
    targets = 0
    for i in range(n):
        l = input().split()
        if "A" in l:
            a_coordinate = [i, l.index("A")]
        if "x" in l:
            targets += l.count("x")
        demo_matrix.append(l)
    return demo_matrix, a_coordinate, targets


rows = 5
matrix, position, targets = create_matrix(rows)
columns = len(matrix[0])
c_row = position[0]
c_col = position[1]
n = int(input())
shoots = []

for i in range(n):
    action, direction, *steps = input().split()
    if action == "move":
        steps = int(steps[0])
        if direction == "left" and columns > c_col - steps >= 0:
            if matrix[c_row][c_col - steps] == ".":
                matrix[c_row][c_col] = "."
                c_col -= steps
                matrix[c_row][c_col] = "A"
        elif direction == "right" and columns > c_col + steps >= 0:
            if matrix[c_row][c_col + steps] == ".":
                matrix[c_row][c_col] = "."
                c_col += steps
                matrix[c_row][c_col] = "A"
        elif direction == "up" and rows > c_row - steps >= 0:
            if matrix[c_row - steps][c_col] == ".":
                matrix[c_row][c_col] = "."
                c_row -= steps
                matrix[c_row][c_col] = "A"
        elif direction == "down" and rows > c_row + steps >= 0:
            if matrix[c_row + steps][c_col] == ".":
                matrix[c_row][c_col] = "."
                c_row += steps
                matrix[c_row][c_col] = "A"
    elif action == "shoot":
        if direction == "left":
            for c in range(c_col, -1, -1):
                if matrix[c_row][c] == "x":
                    matrix[c_row][c] = "."
                    shoots.append([c_row, c])
                    targets -= 1
                    break
        elif direction == "right":
            for c in range(c_col, columns):
                if matrix[c_row][c] == "x":
                    matrix[c_row][c] = "."
                    shoots.append([c_row, c])
                    targets -= 1
                    break
        elif direction == "up":
            for r in range(c_row, -1, -1):
                if matrix[r][c_col] == "x":
                    matrix[r][c_col] = "."
                    shoots.append([r, c_col])
                    targets -= 1
                    break
        elif direction == "down":
            for r in range(c_row, rows):
                if matrix[r][c_col] == "x":
                    matrix[r][c_col] = "."
                    shoots.append([r, c_col])
                    targets -= 1
                    break
    if targets == 0:
        break

if targets == 0:
    print(f"Training completed! All {len(shoots)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

print("\n".join(str(el) for el in shoots))
