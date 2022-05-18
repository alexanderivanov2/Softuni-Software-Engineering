import re

text = input()
pattern_digits = r"\d"
pattern = r"(\:\:|\*\*)(?P<name>[A-Z][a-z]{2,})\1"
emojies = re.findall(pattern, text)
digits = re.findall(pattern_digits, text)

total = 1

for digit in digits:
    total *= int(digit)

print(f"Cool threshold: {total}")
print(f"{len(emojies)} emojis found in the text. The cool ones are:")
for emoji in emojies:
    emoji_colness = sum([ord(el) for el in emoji[1]])
    if emoji_colness > total:
        print(f"{emoji[0]}{emoji[1]}{emoji[0]}")