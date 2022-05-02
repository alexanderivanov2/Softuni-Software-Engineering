rage_message = input()
convert_message = ""
collect_chars = ""
unique_symbols = []

for i in range(len(rage_message)):
    char = rage_message[i]
    if not char.isdigit() and char.upper() not in unique_symbols:
        unique_symbols.append(char.upper())
    if not char.isdigit():
        collect_chars += char.upper()
    else:
        if len(rage_message) > i + 1:
            if rage_message[i + 1].isdigit():
                char += rage_message[i + 1]
        convert_message += collect_chars * int(char)
        collect_chars = ''
        if len(rage_message) <= i + 2:
            break

print(f"Unique symbols used: {len(unique_symbols)}")
print(convert_message)