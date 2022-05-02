import string

total = 0
current_total = 0
combinations = input().split()

for combination in combinations:
    first_letter = combination[0]
    last_letter = combination[-1]
    number = int(combination[1:-1])
    current_total = 0
    if first_letter.isupper():
        position = string.ascii_uppercase.index(first_letter) + 1
        current_total += number / position
    else:
        position = string.ascii_lowercase.index(first_letter) + 1
        current_total += number * position

    if last_letter.isupper():
        position = string.ascii_uppercase.index(last_letter) + 1
        current_total -= position
    else:
        position = string.ascii_lowercase.index(last_letter) + 1
        current_total += position
    total += current_total
print(f"{total:.2f}")