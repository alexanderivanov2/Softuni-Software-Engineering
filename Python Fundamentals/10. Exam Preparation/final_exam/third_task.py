users = {}

command = input()

while not command == "Log out":
    action, username, *data = command.split(": ")
    if action == "New follower" and username not in users:
        users[username] = {'likes': 0, 'comments': 0}
    elif action == "Like":
        count = int(data[0])
        if username not in users:
            users[username] = {'likes': count, 'comments': 0}
        else:
            users[username]['likes'] += count
    elif action == "Comment":
        if username not in users:
            users[username] = {'likes': 0, 'comments': 1}
        else:
            users[username]['comments'] += 1
    elif action == "Blocked":
        if username not in users:
            print(f"{username} doesn't exist.")
        else:
            del users[username]
    command = input()

combine_users = {}
for key in users:
    combine_users[key] = users[key]['likes'] + users[key]['comments']

sorted_cu = dict(sorted(combine_users.items(), key=lambda x: (-x[1], x)))

print(f"{len(sorted_cu)} followers")
for key, value in sorted_cu.items():
    print(f"{key}: {value}")