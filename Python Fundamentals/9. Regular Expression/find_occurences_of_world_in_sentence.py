import re

text = input().lower()
word = input().lower()
pattern = rf"\b{word}\b"

print(len(re.findall(pattern, text)))