import re

n = int(input())
pattern_name = r"\@([A-Za-z]+)\|"
pattern_age = r"#(\d+)\*"
for i in range(n):
    text = input()
    find_name = re.findall(pattern_name, text)
    find_age = re.findall(pattern_age, text)
    print(f"{find_name[0]} is {find_age[0]} years old.")
