courses = {}
command = input()

while ':' in command:
    name, _id, course = command.split(":")
    if course not in courses:
        courses[course] = []
    courses[course].append(f"{name} - {int(_id)}")
    command = input()

if command in courses:
    [print(x) for x in courses[command]]
else:
    command = command.replace('_', ' ')
    [print(x) for x in courses[command]]