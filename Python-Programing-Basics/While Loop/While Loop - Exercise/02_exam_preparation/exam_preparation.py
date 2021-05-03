bad_grades = int(input())
count_bad_grades = 0
grades = []
subjects = []
subject = input()
pass_or_not = True

while subject != "Enough":
    subjects.append(subject)
    grade = int(input())
    grades.append(grade)
    if grade <= 4:
        count_bad_grades += 1
        if count_bad_grades >= bad_grades:
            print(f"You need a break, {bad_grades} poor grades.")
            exit()
    subject = input()

average_score = sum(grades) / len(grades)
print(f"Average score: {average_score:.2f}")
print(f"Number of problems: {len(grades)}")
print(f"Last problem: {subjects[-1]}")