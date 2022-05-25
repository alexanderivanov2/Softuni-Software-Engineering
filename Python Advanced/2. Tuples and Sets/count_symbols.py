text = input()
symbols = tuple([x for x in text])
dict_symbols = {}
for el in symbols:
    if el not in dict_symbols:
        dict_symbols[el] = symbols.count(el)

dict_symbols = dict(sorted(dict_symbols.items(), key=lambda x: x))

for key, value in dict_symbols.items():
    print(f"{key}: {value} time/s")
