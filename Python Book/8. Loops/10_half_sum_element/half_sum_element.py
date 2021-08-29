n = int(input())
max_number = -10000000000
sum_of_all = 0
sum = 0

for i in range(n):
    num = int(input())
    if num > max_number:
        max_number = num
    sum_of_all += num
    sum = sum_of_all - max_number

if max_number == sum:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_number - sum)}")