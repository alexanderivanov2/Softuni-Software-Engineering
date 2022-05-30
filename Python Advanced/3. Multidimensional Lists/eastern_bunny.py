def create_matrix(n):
    demo_matrix = []
    b_coordinate = []
    for i in range(n):
        l = input().split()
        if "B" in l:
            b_coordinate = [i, l.index("B")]
        demo_matrix.append(l)
    return demo_matrix, b_coordinate


rows = int(input())
matrix, bunny = create_matrix(rows)
columns = len(matrix[0])

max_sum = 0
side = None
dict_sides = {"right": [], "left": [], "up": [], "down": []}

row = bunny[0]
col = bunny[1]
# right
sum = 0
for c in range(col + 1, columns):
    if matrix[row][c] == "X":
        break
    sum += int(matrix[row][c])
    dict_sides["right"].append([row, c])
if sum > max_sum:
    max_sum = sum
    side = "right"

# left
sum = 0
for c in range(col - 1, -1, -1):
    if matrix[row][c] == "X":
        break
    sum += int(matrix[row][c])
    dict_sides["left"].append([row, c])
if sum > max_sum:
    max_sum = sum
    side = "left"

# up
sum = 0
for r in range(row - 1, -1, -1):
    if matrix[r][col] == "X":
        break
    sum += int(matrix[r][col])
    dict_sides["up"].append([r, col])
if sum > max_sum:
    max_sum = sum
    side = "up"

#down
sum = 0
for r in range(row + 1, rows):
    if matrix[r][col] == "X":
        break
    sum += int(matrix[r][col])
    dict_sides["down"].append([r, col])
if sum > max_sum:
    max_sum = sum
    side = "down"

if side:
    print(side)
    print("\n".join(str(el) for el in dict_sides[side]))
    print(max_sum)
else:
    print("")
    print()
    print(float('-inf'))