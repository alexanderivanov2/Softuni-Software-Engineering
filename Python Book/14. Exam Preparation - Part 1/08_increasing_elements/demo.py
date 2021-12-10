n = int(input())
maximum = 0
last_num = 0
total = 0

for i in range(1, n + 1):
    increasing = int(input())
    if increasing > last_num:
        last_num = increasing
        maximum += 1
        if maximum > total:
            total = maximum
    else:
        last_num = increasing
        maximum = 1

print(total)