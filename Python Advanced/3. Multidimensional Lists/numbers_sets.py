first = set(int(el) for el in input().split())
second = set(int(el) for el in input().split())
n = int(input())

for i in range(n):
    command, direction, *sequence = input().split()
    if command == "Check":
        print(True if first.issubset(second) or second.issubset(first) else False)
        continue
    sequence = set(int(el) for el in sequence)
    if command == "Add" and direction == "First":
        first.update(sequence)
    elif command == "Add" and direction == "Second":
        second.update(sequence)
    elif command == "Remove" and direction == "First":
        first.difference_update(sequence)
    elif command == "Remove" and direction == "Second":
        second.difference_update(sequence)


print(", ".join(str(el) for el in sorted(first)))
print(", ".join(str(el) for el in sorted(second)))