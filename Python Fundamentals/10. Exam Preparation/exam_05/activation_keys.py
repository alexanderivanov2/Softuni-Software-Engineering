key = input()

command = input()

while not command == "Generate":
    action, *data = command.split(">>>")
    if action == 'Contains':
        if data[0] in key:
            print(f"{key} contains {data[0]}")
        else:
            print("Substring not found!")
    elif action == 'Flip':
        flip = data[0].lower()
        start_index = int(data[1])
        end_index = int(data[2])
        changed_part = key[start_index:end_index]
        changed_part_action = changed_part.lower() if flip == "lower" else changed_part.upper()
        key = key.replace(changed_part, changed_part_action)
        print(key)
    elif action == 'Slice':
        start_index = int(data[0])
        end_index = int(data[1])
        part = key[start_index:end_index]
        key = key.replace(part, "")
        print(key)
    command = input()

print(f"Your activation key is: {key}")