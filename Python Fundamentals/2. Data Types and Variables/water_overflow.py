CAPACITY = 255
capacity = 255
n = int(input())

for _ in range(n):
    num = int(input())
    if num <= capacity:
        capacity -= num
    else:
        print("Insufficient capacity!")

print(CAPACITY - capacity)
