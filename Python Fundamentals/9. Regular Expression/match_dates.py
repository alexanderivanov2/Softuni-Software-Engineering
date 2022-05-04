import re

dates = input()
patern = r"(?P<day>\d{2})([\-\.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"

dates_match = re.findall(patern, dates)

for date in dates_match:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")