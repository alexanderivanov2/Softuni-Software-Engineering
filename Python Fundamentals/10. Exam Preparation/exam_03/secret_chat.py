message = input()
command = input()

while not command == "Reveal":
    action, *data = command.split(":|:")
    if action == "InsertSpace":
        index = int(data[0])
        message = message[:index] + " " + message[index:]
        print(message)
    elif action == "Reverse":
        substring = data[0]
        if substring not in message:
            print("error")
        else:
            new_substring = substring[::-1]
            message = message.replace(substring, "", 1)
            message += new_substring
            print(message)
    elif action == "ChangeAll":
        substring = data[0]
        replacement = data[1]
        message = message.replace(substring, replacement)
        print(message)
    command = input()

print(f"You have a new text message: {message}")

