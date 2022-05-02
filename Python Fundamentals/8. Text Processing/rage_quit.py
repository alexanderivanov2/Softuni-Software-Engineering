txt = input()
rage = ''
repeat = 0
symbols_used = 0
repeat_string = ''

for i in range(len(txt)):
    if txt[i].isdigit():
        repeat = ''
        repeat += txt[i]
        if i == len(txt) - 1 or not txt[i+1].isdigit():
            repeat_string += rage * int(repeat)
            rage = ''
        continue
    elif txt[i].isalpha():
        rage += txt[i].upper()
    else:
        rage += txt[i]

set_string = set(repeat_string)
print(f"Unique symbols used: {len(set_string)}")
print(repeat_string)