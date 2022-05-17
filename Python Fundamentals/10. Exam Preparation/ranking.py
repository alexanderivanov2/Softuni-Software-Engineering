def check_result(modules_d, modul, pword):
    if modul in modules_d:
        if pword == modules_d[modul]:
            return True
        else:
            return False
    else:
        return False

courses = {}
users = {}
users_total_points = {}
course = input()
while not course == 'end of contests':
    name, password = course.split(":")
    if name not in courses:
        courses[name] = password
    course = input()

candidate = input()
while not candidate == 'end of submissions':
    name, password, user, points = candidate.split("=>")
    check = check_result(courses, name, password)
    if check:
        if user not in users:
            users[user] = {name: int(points)}
            users_total_points[user] = int(points)
        elif name not in users[user]:
            users[user][name] = int(points)
            users_total_points[user] += int(points)
        elif users[user][name] < int(points):
            users_total_points[user] -= users[user][name]
            users[user][name] = int(points)
            users_total_points[user] += int(points)
    candidate = input()

sorted_total = dict(sorted(users_total_points.items(), key=lambda x: -x[1]))
for key, value in sorted_total.items():
    print(f"Best candidate is {key} with total {value} points.")
    break

sorted_users = dict(sorted(users.items(), key=lambda x: x[0]))
print("Ranking:")
for key, value in sorted_users.items():
    print(key)
    sorted_courses = dict(sorted(value.items(), key=lambda x: -x[1]))
    for key, value in sorted_courses.items():
        print(f"#  {key} -> {value}")