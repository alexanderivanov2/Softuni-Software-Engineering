end = int(input())
start = int(input())
s = int(input())

for i in range(start, end - 1, -1):
    if i % 2 == 0 and i % 3 == 0:
        if i != s:
            print(f"{i}", end=" ")
        else:
            exit()