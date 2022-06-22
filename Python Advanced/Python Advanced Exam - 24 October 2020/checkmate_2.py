matrix = []
k_r = 0
k_c = 0

for i in range(8):
    line = input().split()
    if "K" in line:
        k_r = i
        k_c = line.index("K")
    matrix.append(line)

checkmates = []

#check_up
if True:
    c_r = k_r - 1
    c_c = k_c
    while c_r >= 0:
        if matrix[c_r][c_c] == "Q":
            checkmates.append([c_r, c_c])
            break
        c_r -= 1

# check_right_top_diagonal
if True:
    c_r = k_r - 1
    c_c = k_c + 1
    while c_c <= 7 and c_r >= 0:
        if matrix[c_r][c_c] == "Q":
            checkmates.append([c_r, c_c])
            break
        c_r -= 1
        c_c += 1

# check right
if True:
    c_r = k_r
    c_c = k_c + 1
    while c_c <= 7:
        if matrix[c_r][c_c] == "Q":
            checkmates.append([c_r, c_c])
            break
        c_c += 1


# check_right_down_diagonal
if True:
    c_r = k_r + 1
    c_c = k_c + 1
    while c_c <= 7 and c_r <= 7:
        if matrix[c_r][c_c] == "Q":
            checkmates.append([c_r, c_c])
            break
        c_c += 1
        c_r += 1

#check_down
if True:
    c_r = k_r + 1
    while c_r <= 7:
        if matrix[c_r][k_c] == "Q":
            checkmates.append([c_r, k_c])
            break
        c_r += 1

#check_left_down_diagonal
if True:
    c_r = k_r + 1
    c_c = k_c - 1
    while c_c >= 0 and c_r <= 7:
        if matrix[c_r][c_c] == "Q":
            checkmates.append([c_r, c_c])
            break
        c_c -= 1
        c_r += 1

#check_left
if True:
    c_r = k_r
    c_c = k_c - 1
    while c_c >= 0:
        if matrix[c_r][c_c] == "Q":
            checkmates.append([c_r, c_c])
            break
        c_c -= 1

#check_left_top_diagonal
if True:
    c_r = k_r - 1
    c_c = k_c - 1
    while c_c >= 0 and c_r >= 0:
        if matrix[c_r][c_c] == "Q":
            checkmates.append([c_r, c_c])
            break
        c_r -= 1
        c_c -= 1


if checkmates:
    for ch in checkmates:
        print(ch)
else:
    print("The king is safe!")
