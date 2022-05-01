students = {}
n = int(input())

for i in range(n):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = []
    students[student].append(grade)

passed_students = {}

for key, value in students.items():
    new_value = sum(value) / len(value)
    if new_value >= 4.50:
        passed_students[key] = new_value


sorted_dict = dict(sorted(passed_students.items(), key=lambda x: -x[1]))

for key, value in sorted_dict.items():
    print(f"{key} -> {value:.2f}")