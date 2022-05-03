string_explosion = input()
explosion = 0
after_explosion = ""

for i in range(len(string_explosion)):
    if string_explosion[i] == ">":
        after_explosion += string_explosion[i]
        explosion += int(string_explosion[i + 1])
        continue
    elif explosion > 0:
        explosion -= 1
        continue
    else:
        after_explosion += string_explosion[i]

print(after_explosion)


