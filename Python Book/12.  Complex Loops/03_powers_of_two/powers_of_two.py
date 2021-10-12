n = int(input())

for i in range(0, n+1):
    even = 2 ** i
    if even % 2 == 0 or even == 1:
        print(2 ** i)