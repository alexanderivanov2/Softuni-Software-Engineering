from math import floor


def find_player_cordinates(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "P":
                return row, col


def calculate_losses(coins):
    return floor(coins * 0.50)


n = int(input())
matrix = [[x for x in input().split()] for i in range(n)]
row, col = find_player_cordinates(matrix)
sides = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}
coins = 0
status = True
my_path = []

while coins < 100:
    path = input()
    row += sides[path][0]
    col += sides[path][1]
    if 0 > row or row == n or 0 > col or col == n:
        status = False
        coins = calculate_losses(coins)
        break

    if matrix[row][col] == "X":
        coins = calculate_losses(coins)
        status = False
        break

    coins += int(matrix[row][col])
    my_path.append([row, col])

if status:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
for el in my_path:
    print(el)
