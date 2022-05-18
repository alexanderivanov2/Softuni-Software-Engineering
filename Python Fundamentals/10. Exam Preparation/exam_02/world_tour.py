stops = input()

command = input()

while not command == "Travel":
    action, *data = command.split(":")
    if action == "Add Stop":
        index = int(data[0])
        string = data[1]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif action == "Remove Stop":
        start_index = int(data[0])
        end_index = int(data[1])
        if len(stops) > start_index >= 0 and len(stops) > end_index >= 0:
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)
    elif action == "Switch":
        old_string = data[0]
        new_string = data[1]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
