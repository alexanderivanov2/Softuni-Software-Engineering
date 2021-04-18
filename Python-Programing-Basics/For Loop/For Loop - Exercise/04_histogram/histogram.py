def calclulate_procent(num1, n2):
    return num1 / n2 * 100


n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num < 400:
        p2 += 1
    elif 399 < num < 600:
        p3 += 1
    elif 599 < num < 800:
        p4 += 1
    else:
        p5 += 1


print(f"{calclulate_procent(p1,n):.2f}%\n{calclulate_procent(p2,n):.2f}%\n{calclulate_procent(p3,n):.2f}%")
print(f"{calclulate_procent(p4,n):.2f}%\n{calclulate_procent(p5,n):.2f}%")
