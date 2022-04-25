text = input().replace(' ', '')

characters_dict = {}

for c in text:
    if c not in characters_dict:
        characters_dict[c] = 0
    characters_dict[c] += 1

[print(f"{key} -> {value}") for key, value in characters_dict.items()]