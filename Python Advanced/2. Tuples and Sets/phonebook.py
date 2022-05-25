user = input()
users = {}
while not user.isdigit():
    name, number = user.split("-")
    if name not in users:
        users[name] = number
    user = input()

n = int(user)

for _ in range(n):
    name = input()
    if name in users:
        print(f"{name} -> {users[name]}")
    else:
        print(f"Contact {name} does not exist.")
