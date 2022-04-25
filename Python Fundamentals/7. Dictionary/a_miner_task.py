resources_statistics = {}
counter = 1
resource_type = None

command = input()

while not command == 'stop':
    if counter % 2 == 0:
        if resource_type not in resources_statistics:
            resources_statistics[resource_type] = 0
        resources_statistics[resource_type] += int(command)
    else:
        resource_type = command
    counter += 1
    command = input()

[print(f"{key} -> {value}") for key, value in resources_statistics.items()]
