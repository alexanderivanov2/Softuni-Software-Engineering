from collections import deque

main_colors = {"red": 0, "yellow": 0, "blue": 0}
secondary_colors = {"orange": 0, "purple": 0, "green": 0}
colors = []
# orange = red + yellow
# purple = red + blue
# green  = yellow + blue
string_colors = deque(input().split())

while len(string_colors) > 1:
    first = string_colors.popleft()
    last = string_colors.pop()
    first_last = first + last
    last_first = last + first
    if first_last in main_colors or first_last in secondary_colors:
        colors.append(first_last)
    elif last_first in main_colors or last_first in secondary_colors:
        colors.append(last_first)
    else:
        middle_index = len(string_colors) // 2
        first_last_cut = first[:-1]
        last_first_cut = last[:-1]
        if last_first_cut:
            string_colors.insert(middle_index, last_first_cut)
        if first_last_cut:
            string_colors.insert(middle_index, first_last_cut)

if string_colors:
    color = string_colors.pop()
    if color in main_colors or color in secondary_colors:
        colors.append(color)

for c in range(len(colors)):
    if colors[c] in secondary_colors:
        if colors[c] == "orange" and ("red" not in colors or "yellow" not in colors):
            colors[c] = None
        elif colors[c] == "purple" and ("red" not in colors or "blue" not in colors):
            colors[c] = None
        elif colors[c] == "green" and ("blue" not in colors or "yellow" not in colors):
            colors[c] = None

colors = [el for el in colors if el]
a = 5
print(colors)
