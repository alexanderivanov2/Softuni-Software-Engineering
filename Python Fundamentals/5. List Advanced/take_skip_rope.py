text = input()
digits = [int(el) for el in text if el.isdigit()]
strings = [el for el in text if not el.isdigit()]
take_list = [digits[i] for i in range(0, len(digits), 2)]
skip_list = [digits[i] for i in range(1, len(digits), 2)]
new_string = ""
index = 0
for i in range(len(take_list)):
    if not take_list[i] == 0:
        new_string += ''.join(strings[index: index + take_list[i]])
        index += take_list[i]
    index += skip_list[i]

print(new_string)