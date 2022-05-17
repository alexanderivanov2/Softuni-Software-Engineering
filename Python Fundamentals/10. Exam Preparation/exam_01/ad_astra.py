import re
from math import floor

PER_DAY_KCAL = 2000
txt = input()
pattern = r"(#|\|)(?P<item_name>[A-Za-z\s]+)\1(?P<expiration_date>[0-3][0-9]\/[0-1][0-9]\/\d{2})\1(?P<calories>\d+)\1"
items = []
total_kcal = 0

a = 5
for match in re.finditer(pattern, txt):
    items.append(f"Item: {match.group('item_name')}, Best before: {match.group('expiration_date')}, Nutrition: {match.group('calories')}")
    total_kcal += int(match.group('calories'))

print(f"You have food to last you for: {floor(total_kcal / PER_DAY_KCAL)} days!")
if items:
    print('\n'.join(items))
