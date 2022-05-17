contests = {}
individual_users = {}
txt = input()

while not txt == "no more time":
    user, contest, points = txt.split(" -> ")
    points = int(points)
    if user not in individual_users:
        individual_users[user] = 0
    if contest not in contests:
        contests[contest] = {user: points}
        individual_users[user] += points
    elif user not in contests[contest]:
        contests[contest][user] = points
        individual_users[user] += points
    elif contests[contest][user] < points:
        individual_users[user] -= contests[contest][user]
        individual_users[user] += points
        contests[contest][user] = points

    txt = input()

for key, value in contests.items():
    print(f"{key}: {len(value)} participants")
    counter = 1
    sorted_value = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
    for name, points in sorted_value.items():
        print(f"{counter}. {name} <::> {points}")
        counter += 1

print("Individual standings: ")
sorted_individual = dict(sorted(individual_users.items(), key=lambda x: (-x[1], x[0])))

counter = 1
for key, value in sorted_individual.items():
    print(f"{counter}. {key} -> {value}")
    counter += 1