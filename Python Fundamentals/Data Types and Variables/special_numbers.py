n = int(input())

for i in range(1, n + 1):
    if sum([int(num) for num in str(i)]) in [5, 7, 11]:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
