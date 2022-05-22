txt = [x for x in input()]
reverse_txt = ''

for i in range(len(txt)):
    a = txt.pop()
    reverse_txt += a

print("".join(reverse_txt))
