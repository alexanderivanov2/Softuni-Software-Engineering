def create_matrix(n):
    matrix = []
    for i in range(n):
        line = [0] * n
        matrix.append(line)
    return matrix


rows = int(input())
columns = rows
bombs = int(input())
matrix = create_matrix(rows)

for b in range(bombs):
    coordinates = input()
    coordinates = coordinates[1:-1].split(", ")
    r = int(coordinates[0])
    c = int(coordinates[1])
    matrix[r][c] = "*"

for r in range(rows):
    for c in range(columns):
        if not matrix[r][c] == "*":
            count = 0
            #left_corner_top
            if r == 0 and c == 0:
                if matrix[r][c + 1] == "*":
                    count += 1
                if matrix[r + 1][c + 1] == "*":
                    count += 1
                if matrix[r + 1][c] == "*":
                    count += 1
            # right_corner_top
            elif r == 0 and c == columns - 1:
                if matrix[r][c - 1] == "*":
                    count += 1
                if matrix[r + 1][c - 1] == "*":
                    count += 1
                if matrix[r + 1][c] == "*":
                    count += 1
            # right_corner_down
            elif r == rows - 1 and c == columns - 1:
                if matrix[r][c - 1] == "*":
                    count += 1
                if matrix[r - 1][c - 1] == "*":
                    count += 1
                if matrix[r - 1][c] == "*":
                    count += 1
            # left_corner_down
            elif r == rows - 1 and c == 0:
                if matrix[r][c + 1] == "*":
                    count += 1
                if matrix[r - 1][c + 1] == "*":
                    count += 1
                if matrix[r - 1][c] == "*":
                    count += 1
            elif r == 0:
                if matrix[r][c + 1] == "*":
                    count += 1
                if matrix[r][c - 1] == "*":
                    count += 1
                if matrix[r + 1][c + 1] == "*":
                    count += 1
                if matrix[r + 1][c - 1] == "*":
                    count += 1
                if matrix[r + 1][c] == "*":
                    count += 1
            elif r == rows - 1:
                if matrix[r][c + 1] == "*":
                    count += 1
                if matrix[r][c - 1] == "*":
                    count += 1
                if matrix[r - 1][c + 1] == "*":
                    count += 1
                if matrix[r - 1][c - 1] == "*":
                    count += 1
                if matrix[r - 1][c] == "*":
                    count += 1
            elif c == 0:
                if matrix[r - 1][c] == "*":
                    count += 1
                if matrix[r - 1][c + 1] == "*":
                    count += 1
                if matrix[r][c + 1] == "*":
                    count += 1
                if matrix[r + 1][c + 1] == "*":
                    count += 1
                if matrix[r + 1][c] == "*":
                    count += 1
            elif c == columns - 1:
                if matrix[r - 1][c] == "*":
                    count += 1
                if matrix[r - 1][c - 1] == "*":
                    count += 1
                if matrix[r][c - 1] == "*":
                    count += 1
                if matrix[r + 1][c - 1] == "*":
                    count += 1
                if matrix[r + 1][c] == "*":
                    count += 1

            else:
                if matrix[r - 1][c] == "*":
                    count += 1
                if matrix[r - 1][c + 1] == "*":
                    count += 1
                if matrix[r][c + 1] == "*":
                    count += 1
                if matrix[r + 1][c + 1] == "*":
                    count += 1
                if matrix[r + 1][c] == "*":
                    count += 1
                if matrix[r + 1][c - 1] == "*":
                    count += 1
                if matrix[r][c - 1] == "*":
                    count += 1
                if matrix[r - 1][c - 1] == "*":
                    count += 1
            matrix[r][c] = count

for l in matrix:
    print(" ".join(str(el) for el in l))
