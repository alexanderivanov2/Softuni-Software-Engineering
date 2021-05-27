locations = int(input())

for location in range(locations):
    average_mine = float(input())
    days = int(input())
    total = 0
    for day in range(days):
        gold = float(input())
        total += gold
    average = total / days
    if average >= average_mine:
        print(f"Good job! Average gold per day: {average:.2f}.")
    else:
        print(f"You need {average_mine - average:.2f} gold.")