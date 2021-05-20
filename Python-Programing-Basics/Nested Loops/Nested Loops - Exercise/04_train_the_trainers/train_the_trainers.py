count = int(input())
total_count = 0
total_grades = 0
subject = input()

while subject != "Finish":
    total_count += count
    grades = 0
    for i in range(count):
        grades += float(input())
    print(f"{subject} - {grades / count:.2f}.")
    total_grades += grades
    grades = 0
    subject = input()

print(f"Student's final assessment is {total_grades / total_count:.2f}.")
