password = input()

command = input()

while not command == "Done":
    action, *data = command.split()
    if action == "TakeOdd":
        new_password = [password[i] for i in range(1, len(password), 2)]
        password = ''.join(new_password)
        print(password)
    elif action == "Cut":
        index = int(data[0])
        length = index + int(data[1])
        password = password[:index] + password[length:]
        print(password)
    elif action == "Substitute":
        substring = data[0]
        substitute = data[1]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {password}")