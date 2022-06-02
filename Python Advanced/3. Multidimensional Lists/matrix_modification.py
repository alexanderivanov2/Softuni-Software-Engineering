matrix = []
rows = int(input())
for i in range(rows):
    line = [int(el) for el in input().split()]
    matrix.append(line)
columns = len(matrix[0])

command = input()
while not command == "END":
    action, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if not rows > row >= 0 or not columns > col >= 0:
        print("Invalid coordinates")
    elif action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value
    command = input()

for l in matrix:
    print(' '.join(str(el) for el in l))

