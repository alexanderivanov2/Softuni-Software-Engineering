characters = input().split(", ")

ascii_values_dict = {}

for c in characters:
    ascii_values_dict[c] = ord(c)

print(ascii_values_dict)