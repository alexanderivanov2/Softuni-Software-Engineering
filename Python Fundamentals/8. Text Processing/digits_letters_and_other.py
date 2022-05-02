word = input()
digits = ''
letters = ''
others = ''
for ch in word:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        others += ch

print(digits)
print(letters)
print(others)