notes = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    priority, to_do = command.split("-")
    priority = int(priority)
    notes[priority - 1] = to_do


result = [el for el in notes if el != 0]
print(result)
