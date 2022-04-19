items = input().split(", ")
command = input()

while not command == "Craft!":
    action, *data = command.split(" - ")
    if action == "Collect" and data[0] not in items:
        items.append(data[0])
    elif action == "Drop" and data[0] in items:
        items.remove(data[0])
    elif action == "Combine Items":
        old_item, new_item = data[0].split(":")
        if old_item in items:
            index = items.index(old_item)
            items.insert(index + 1, new_item)
    elif action == "Renew" and data[0] in items:

        items.pop(items.index(data[0]))
        items.append(data[0])
    command = input()

print(", ".join(items))