encrypted_message = input()

command = input()

while not command == "Decode":
    action, *data = command.split("|")
    if action == "Move":
        num_letters = int(data[0])
        move_part = encrypted_message[:num_letters]
        encrypted_message = encrypted_message[num_letters:] + move_part
    elif action == "Insert":
        index = int(data[0])
        value = data[1]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif action == "ChangeAll":
        substring = data[0]
        replacement = data[1]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {encrypted_message}")