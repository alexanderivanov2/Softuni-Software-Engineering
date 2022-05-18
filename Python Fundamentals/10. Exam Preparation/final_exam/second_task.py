import re

pattern = r"\|(?P<name>[A-Z]{4,})\|\:\#(?P<title>[A-Za-z]+\s[A-Za-z]+)\#"

n = int(input())

for i in range(n):
    txt = input()
    if re.match(pattern, txt):
        for match in re.finditer(pattern, txt):
            print(f"{match.group('name')}, The {match.group('title')}\n>> Strength: {len(match.group('name'))}\n>> Armor: {len(match.group('title'))}")
    else:
        print("Access denied!")
