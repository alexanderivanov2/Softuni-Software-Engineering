import os


def create_file(file_name):
    with open(f"{file_name}", "w") as file:
        return


def add_to_file(file_name, context):
    with open(f"{file_name}", "a") as add_file:
        add_file.write(context + "\n")


def replace_in_file(file_name, old_string, new_string):
    try:
        with open(f"{file_name}", "rt") as files:
            data = files.read()
            data = data.replace(old_string, new_string)
        with open(f"{file_name}", "w") as replace_file:
            replace_file.write(data)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    try:
        os.remove(f"{file_name}")
    except FileNotFoundError:
        print("An error occurred")


def commands_complete():
    command = input()
    while command != "END":
        task, *data = command.split("-")
        if task == "Create":
            create_file(data[0])
        elif task == "Add":
            add_to_file(data[0], data[1])
        elif task == "Replace":
            replace_in_file(data[0], data[1], data[2])
        elif task == "Delete":
            delete_file(data[0])
        command = input()


commands_complete()

# input:
# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End
