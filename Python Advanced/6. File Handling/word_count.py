import re

with open('08-File-Handling-Lab-Resources/Words Count/words.txt', "r") as file:
    list_words = [word for word in file.readline().split()]

dict_counter = {}
with open('08-File-Handling-Lab-Resources/Words Count/text.txt', "r") as file:
    text = ''.join(file.read())
    print(text)
    for word in list_words:
        pattern = rf"\b{word}\b"
        dict_counter[word] = len(re.findall(pattern, text, re.IGNORECASE))

dict_sort = sorted(dict_counter.items(),key=lambda x: (-x[1], x))


for data in dict_sort:
    print(f"{data[0]} - {data[1]}")