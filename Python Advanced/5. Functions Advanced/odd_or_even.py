command = input()
numbers = list(map(int, input().split()))

if command == "Odd":
    print(sum([n for n in numbers if n % 2 != 0]) * len(numbers))
else:
    print(sum([n for n in numbers if n % 2 == 0]) * len(numbers))
