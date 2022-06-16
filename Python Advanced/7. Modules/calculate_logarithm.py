from math import log

number = int(input())
second_line = input()

if second_line == "natural":
    print(f"{log(number):.2f}")
else:
    print(f"{log(10, int(second_line)):.2f}")
