divisor = int(input())
bound = int(input())

for i in range(bound, 0, -1):
    if i % divisor == 0:
        print(i)
        break
