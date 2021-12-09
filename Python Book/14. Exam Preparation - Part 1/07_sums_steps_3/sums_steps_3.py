n = int(input())
sum1, sum2, sum3 = 0, 0, 0

for i in range(1, n + 1):
    num = int(input())
    if i % 3 == 1:
        sum1 += num
    elif i % 3 == 2:
        sum2 += num
    else:
        sum3 += num

print(f"sum1 = {sum1}\nsum2 = {sum2}\nsum3 = {sum3}")