def calculate_procentege(num1, n1):
    return num1 / n1 * 100


n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        p1 += 1

    if num % 3 == 0:
        p2 += 1

    if num % 4 == 0:
        p3 += 1

print(f"{calculate_procentege(p1, n):.2f}%\n{calculate_procentege(p2, n):.2f}%\n{calculate_procentege(p3, n):.2f}%")
