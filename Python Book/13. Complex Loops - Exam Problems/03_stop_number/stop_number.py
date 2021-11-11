N = int(input())
M = int(input())
S = int(input())


for num in range(M, N - 1, - 1):
    if num % 2 == 0 and num % 3 == 0:
        if num == S:
            break
        print(num, end=" ")