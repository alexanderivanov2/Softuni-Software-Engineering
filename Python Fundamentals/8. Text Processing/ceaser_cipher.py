txt = input()
cipher = ''

for ch in txt:
    new_ch = ord(ch) + 3
    cipher += chr(new_ch)

print(cipher)