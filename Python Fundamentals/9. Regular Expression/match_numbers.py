import re

numbers = input()
pattern = r"(^|(?<=\s))(-?\d+)(\.\d+)?($|(?=\s))"

find_numbers = re.findall(pattern, numbers)

for number in find_numbers:
    number_print = [el for el in number if not el == ""]
    print(''.join(number_print), end=" ")
