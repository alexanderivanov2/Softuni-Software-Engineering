import re

txt = input().split(", ")
racers = {key: 0 for key in txt}

pattern_name = r"[A-Za-z]"
pattern_numbers = r"\d"

txt = input()

while not txt == "end of race":
    find_name = re.findall(pattern_name, txt)
    name = "".join(find_name)
    if name in racers:
        distance = sum([int(el) for el in re.findall(pattern_numbers, txt)])
        racers[name] += distance
    txt = input()

sorted_racers = dict(sorted(racers.items(), key=lambda x: -x[1]))


win_racers = []
for key in sorted_racers:
    win_racers.append(key)

print(f"1st place: {win_racers[0]}\n2nd place: {win_racers[1]}\n3rd place: {win_racers[2]}")