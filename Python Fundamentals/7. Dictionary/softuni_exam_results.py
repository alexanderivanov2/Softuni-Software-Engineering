users = {}
exams = {}
txt = input()

while not txt == "exam finished":
    user, *data = txt.split("-")
    if data[0] == "banned":
        users.pop(user)
    else:
        stats = int(data[1])
        language = data[0]
        if user not in users:
            users[user] = stats
        elif users[user] < stats:
            users[user] = stats

        if language not in exams:
            exams[language] = 0
        exams[language] += 1

    txt = input()

sorted_users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))
sorted_exams = dict(sorted(exams.items(), key=lambda x: (-x[1], x[0])))

print("Results:")
for key, value in sorted_users.items():
    print(f"{key} | {value}")

print("Submissions:")
for key,value in sorted_exams.items():
    print(f"{key} - {value}")