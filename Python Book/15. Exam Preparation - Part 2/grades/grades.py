students = int(input())
two, three, four, five = 0, 0, 0, 0
total = 0

for i in range(1, students + 1):
    grade = float(input())
    total += grade
    if grade < 3:
        two += 1
    elif grade < 4:
        three += 1
    elif grade < 5:
        four += 1
    else:
        five += 1

print(f"Top students: {five / students * 100:.2f}%\nBetween 4.00 and 4.99: {four / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {three / students * 100:.2f}%\nFail: {two / students * 100:.2f}%")
print(f"Average: {total / students:.2f}")