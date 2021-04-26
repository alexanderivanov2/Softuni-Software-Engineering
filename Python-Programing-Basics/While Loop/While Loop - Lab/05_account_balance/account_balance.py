total = 0
command = input()

while command != "NoMoreMoney":
    command = float(command)
    if command >= 0:
        total += command
        print(f"Increase: {command:.2f}")
    else:
        print("Invalid operation!")
        break
    command = input()

print(f"Total: {total:.2f}")