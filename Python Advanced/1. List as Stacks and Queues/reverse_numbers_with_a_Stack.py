numbers = input().split()
numbers = [int(x) for x in numbers]
reverse_num = []

while numbers:
    reverse_num.append(numbers.pop())

print(*reverse_num)