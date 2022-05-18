import re

pattern = r"(=|\/)(?P<name>[A-Z][A-Za-z]{2,})\1"
txt = input()
destinations = []
travel_points = 0

for match in re.finditer(pattern, txt):
    city = match.group("name")
    destinations.append(city)
    travel_points += len(city)
if destinations:
    print(f"Destinations: {', '.join(destinations)}")
else:
    print("Destinations:")
print(f"Travel Points: {travel_points}")