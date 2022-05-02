txt = input()

for i in range(len(txt)):
    if txt[i] == ":":
        print(txt[i] + txt[i + 1])