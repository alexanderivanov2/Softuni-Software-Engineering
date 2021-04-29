student_name = input()
count = 0
count_fail = 0
grades = []
grade = float(input())

while count < 12:
    if grade < 4:
        count_fail += 1
        if count_fail > 1:
            print(f"{student_name} has been excluded at {count} grade")
            exit()
        grades.append(grade)
    else:
        grades.append(grade)
    count += 1
    if count < 12:
        grade = float(input())


avarage_grade = sum(grades) / len(grades)
print(f"{student_name} graduated. Average grade: {avarage_grade:.2f}")