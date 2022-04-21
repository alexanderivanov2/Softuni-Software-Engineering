line = [int(num) for num in input().split()]
factor = int(input())
happiness = [num * factor for num in line]
average_happiness = sum(happiness) / len(happiness)
happy_line = [n for n in happiness if n >= average_happiness]

if len(happy_line) >= len(happiness) / 2:
    print(f"Score: {len(happy_line)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_line)}/{len(happiness)}. Employees are not happy!")