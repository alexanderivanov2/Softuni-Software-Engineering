energy = 100
coins = 100
events = input().split("|")
bankrut = False


for event in events:
    task, value = event.split("-")
    value = int(value)
    if task == "rest":
        if energy == 100:
            print("You gained 0 energy.")
        else:
            energy += value
            if energy > 100:
                print(f"You gained {value - (energy - 100)} energy.")
                energy = 100
            else:
                print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")
    elif task == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            print("You had to rest!")
            energy += 50
    else:
        if value >= coins:
            bankrut = True
            print(f"Closed! Cannot afford {task}.")
            break
        else:
            coins -= value
            print(f"You bought {task}.")


if not bankrut:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")