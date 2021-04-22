username = input()
password = input()
password_enter = input()

while password_enter != password:
    password_enter = input()

print(f"Welcome {username}!")