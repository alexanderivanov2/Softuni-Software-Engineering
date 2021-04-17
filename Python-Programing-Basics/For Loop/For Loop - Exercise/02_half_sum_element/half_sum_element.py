n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

max_number = max(numbers)
numbers.remove(max_number)

if sum(numbers) == max_number:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_number - sum(numbers))}")