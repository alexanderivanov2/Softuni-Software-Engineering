number = input()
numbers = []

while number != "Stop":
    number = int(number)
    numbers.append(number)
    number = input()

print(max(numbers))