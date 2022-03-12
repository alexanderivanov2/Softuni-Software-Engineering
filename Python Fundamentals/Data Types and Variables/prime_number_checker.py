n = int(input())
ending = n // 2
check = True

for i in range(2, ending):
    if n % i == 0:
        check = False
        break

print(check)