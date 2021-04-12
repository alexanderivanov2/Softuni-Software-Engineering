n = int(input())
left_sum = 0
right_sum = 0
for i in range(1, n * 2 + 1):
    num = int(input())
    if i <= n:
        left_sum += num
    else:
        right_sum += num


if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
