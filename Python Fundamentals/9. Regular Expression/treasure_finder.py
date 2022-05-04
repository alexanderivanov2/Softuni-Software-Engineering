import re

treasure_type = r"\&(.+)\&"
cordinate = r"\<(.+)\>"
keys = [int(el) for el in input().split()]
counter = 0
line = input()

while not line == "find":
    decrypt_text = ''
    for el in line:
        decrypt_text += chr(ord(el) - keys[counter])
        counter += 1
        if counter == len(keys):
            counter = 0
    counter = 0
    type_treasure = re.findall(treasure_type, decrypt_text)
    cordinate_find = re.findall(cordinate, decrypt_text)
    print(f"Found {type_treasure[0]} at {cordinate_find[0]}")
    line = input()