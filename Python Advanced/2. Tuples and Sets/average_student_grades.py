students = {}
n = int(input())

for i in range(n):
    name, data = input().split()
    grade = float(data)
    if name in students:
        students[name].append(grade)
    else:
        students[name] = [grade]

for key, value in students.items():

    print(f"{key} -> ", end="")
    for val in value:
        print(f"{val:.2f}", end=" ")
    print(f"(avg: {sum(value) / len(value):.2f})")
