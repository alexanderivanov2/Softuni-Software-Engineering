string_list = input().split("|")
new_list = []
while string_list:
    current_list = string_list.pop()
    for el in current_list.split():
        new_list.append(el)

print(" ".join(str(el) for el in new_list))