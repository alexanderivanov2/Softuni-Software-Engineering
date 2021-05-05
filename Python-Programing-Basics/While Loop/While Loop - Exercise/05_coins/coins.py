change_coins = float(input())
coins = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
counter = 0

while change_coins > 0:
    for coin in coins:
        if coin <= change_coins:
            counter += 1
            change_coins -= coin
            change_coins = round(change_coins, 2)

            break

print(counter)