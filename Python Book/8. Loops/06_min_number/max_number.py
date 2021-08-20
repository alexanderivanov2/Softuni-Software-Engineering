n = int(input())
max_num = -1000000000000

for i in range(n):
    num = int(input())
    if num > max_num:
        max_num = num

print(max_num)