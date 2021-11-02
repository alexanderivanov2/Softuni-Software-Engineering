n = int(input())
num = 0

for row in range(1, n+1):
    for j in range(row):
        num += 1
        if num > n:
            break
        print(num, end=" ")
    print()