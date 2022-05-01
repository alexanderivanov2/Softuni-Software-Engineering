elements = input().lower().split()
dict_elements = {}

for el in elements:
    if el not in dict_elements:
        dict_elements[el] = 0
    dict_elements[el] += 1

[print(key, end=' ') for key in dict_elements if not dict_elements[key] % 2 == 0]
