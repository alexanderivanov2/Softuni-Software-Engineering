def create_matrix(n):
    demo_matrix = []
    for i in range(n):
        line = input().split()
        demo_matrix.append(line)
    return demo_matrix


rows, columns = [int(i) for i in input().split()]
matrix = create_matrix(rows)

command = input()
while not command == "END":
    if "swap" in command and len(command.split()) == 5:
        r, c, r2, c2 = [int(el) for el in command.split()[1:]]
        if r <= rows >= r2 or c <= columns >= c2:
            matrix[r][c], matrix[r2][c2] = matrix[r2][c2], matrix[r][c]
            for r in matrix:
                print(" ".join(el for el in r))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()
