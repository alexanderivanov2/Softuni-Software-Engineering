def register_action(users, user, plate_number):
    if user not in users:
        users[user] = plate_number
        print(f"{user} registered {plate_number} successfully")
    else:
        print(f"ERROR: already registered with plate number {plate_number}")
    return users

def unregister_action(users, user):
    if user not in users:
        print(f"ERROR: user {user} not found")
    else:
        del users[user]
        print(f"{user} unregistered successfully")
    return users

n = int(input())
users = {}

for i in range(n):
    action, *data = input().split()
    if action == 'register':
        users = register_action(users, data[0], data[1])
    else:
        user = unregister_action(users, data[0])


for key, value in users.items():
    print(f"{key} => {value}")