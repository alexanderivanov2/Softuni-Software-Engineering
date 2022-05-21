n = int(input())
numbers = []
final_sequence = []
for _ in range(n):
    command = input().split()
    key = int(command[0])
    if key == 1:
        num = int(command[1])
        numbers.append(num)
    elif len(numbers) > 0:
        if key == 2:
            numbers.pop()
        elif key == 3 :
            print(max(numbers))
        elif key == 4:
            print(min(numbers))

while numbers:
    final_sequence.append(numbers.pop())

final_sequence = [str(x) for x in final_sequence]
print(", ".join(final_sequence))
