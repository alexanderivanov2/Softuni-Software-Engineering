import re

n = int(input())
attacked_planets = []
destroyed_planets = []
pattern_char = r'[star]'
pattern_planet_info = r"@(?P<name>[A-Za-z]+)[^\@\-\!\:\>]*:(?P<population>\d+)[^\@\-\!\:\>]*!(?P<att_type>[AD])\![^\@\-\!\:\>]*\->(?P<soldiers>\d+)"

for i in range(n):
    text = input()
    num = len(re.findall(pattern_char, text.lower()), )
    new_text = ""
    for el in text:
        new_text += chr(ord(el) - num)
    search_planet_full = re.finditer(pattern_planet_info, new_text)
    if search_planet_full:
        for search_planet in search_planet_full:
            if search_planet.group("att_type") == "A":
                attacked_planets.append(search_planet.group("name"))
            else:
                destroyed_planets.append(search_planet.group('name'))

print(f"Attacked planets: {len(attacked_planets)}")
if attacked_planets:
    print('\n'.join(f"-> {el}" for el in sorted(attacked_planets)))
print(f"Destroyed planets: {len(destroyed_planets)}")
if destroyed_planets:
    print("\n".join(f"-> {el}" for el in sorted(destroyed_planets)))

