def move_user(sides, user, side):
    for key in sides.keys():
        if user in sides[key]:
            sides[key].remove(user)
            if side in sides:
                sides[side].append(user)
            else:
                sides[side] = [user]
            return sides


sides = {}
users = []
command = input()

while not command == "Lumpawaroo":
    if "|" in command:
        side, user = command.split(' | ')
        if user in users:
            command = input()
            continue
        elif side not in sides:
            sides[side] = [user]
            users.append(user)
        else:
            sides[side].append(user)
            users.append(user)
    else:
        user, side = command.split(' -> ')
        if user in users:
            sides = move_user(sides, user, side)
        elif side in sides:
            sides[side].append(user)
            users.append(user)
        else:
            sides[side] = [user]
            users.append(user)
        print(f"{user} joins the {side} side!")
    command = input()

sorted_sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))

for key, value in sorted_sides.items():
    if not value:
        continue
    result = sorted(value)
    print(f"Side: {key}, Members: {len(value)}")
    [print(f"! {user}") for user in result]