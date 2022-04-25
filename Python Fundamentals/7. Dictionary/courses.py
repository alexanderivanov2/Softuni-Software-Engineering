courses = {}
command = input()

while not command == 'end':
    course, user = command.split(" : ")
    if course not in courses:
        courses[course] = [user]
    else:
        courses[course].append(user)
    command = input()

sorted_courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))

for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")
    sorted_value = sorted(value)
    print('\n'.join(f"-- {x}" for x in sorted_value))

