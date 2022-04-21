first_sequence = [el for el in input().split(", ")]
second_sequence = [el for el in input().split(", ")]
substring = []
for sub in first_sequence:
    for word in second_sequence:
        if sub in word and sub not in substring:
            substring.append(sub)

print(substring)