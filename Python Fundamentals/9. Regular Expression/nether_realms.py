import re

split = r"\s*,\s*|,\s*"
info = input()
demons = sorted(re.split(split, info))
check = r"[\s,]"
health_pattern = r"[^0-9+\-*\/.]"
damage = r"[+-]?\d+\.?\d*"
mult_dev = r"[*/]"
demons_final = {}

for demon in demons:
    x = re.findall(check, demon)
    if not x and len(demon) > 0:
        hp = re.findall(health_pattern, demon)
        dmg = re.findall(damage, demon)
        opertators = re.findall(mult_dev, demon)
        health = sum([ord(x) for x in hp])
        damages = sum([float(x) for x in dmg])
        if damages > 0:
            if len(opertators) > 0:
                for operator in opertators:
                    if operator == "*":
                        damages *= 2
                    else:
                        damages /= 2
        else:
            damages = 0
        demons_final[demon] = []
        demons_final[demon].append(f"{health} health, {damages:.2f} damage")

demons_final = dict(sorted(demons_final.items(), key= lambda x: x[0]))

for d in demons_final:
    print(f"{d} - {demons_final[d][0]}")