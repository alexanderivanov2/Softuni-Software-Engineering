txt = input()
replace_txt = txt[0]

for ch in txt:
    if not ch == replace_txt[-1]:
        replace_txt += ch

print(replace_txt)