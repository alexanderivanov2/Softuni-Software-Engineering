n = int(input())

for row in range(1, n + 1):
    print(chr(36), end=" ")
    for col in range(1, row):
        print(chr(36), end=" ")
    print()