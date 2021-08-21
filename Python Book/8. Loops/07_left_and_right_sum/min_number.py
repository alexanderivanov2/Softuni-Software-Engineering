n = int(input())
min_sum = 100000000000

for i in range(n):
    num = int(input())
    if num < min_sum:
        min_sum = num

print(min_sum)
