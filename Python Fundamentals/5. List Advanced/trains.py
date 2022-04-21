n = int(input())
train = [0 for i in range(n)]

command = input()

while not command == "End":
    action, *data = command.split()
    if action == "add":
        train[-1] += int(data[0])
        command = input()
        continue
    index = int(data[0])
    people = int(data[1])
    if action == "insert":
        train[index] += people
    else:
        train[index] -= people
    command = input()

print(train)
