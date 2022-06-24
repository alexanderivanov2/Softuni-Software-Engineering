matrix = []
for i in range(6):
    line = input().split()
    matrix.append(line)

rows = 6
cols = 6
total_points = 0

for throw in range(3):
    coordinates = input()[1:-1]
    r, c = coordinates.split(", ")
    r = int(r)
    c = int(c)
    if 6 > r >= 0 and 6 > c >= 0:
        if matrix[r][c] == "B":
            score = 0
            for i in range(6):
                if matrix[i][c] != "B":
                    score += int(matrix[i][c])
            total_points += score
            matrix[r][c] = "0"

if 200 > total_points > 99:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif 300 > total_points > 199:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
elif total_points > 299:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
