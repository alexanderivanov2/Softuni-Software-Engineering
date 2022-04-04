nums = input().split()
text = [el for el in input()]
new_text = ""
text_len = len(text)

for num in nums:
    text_len = len(text)
    num = sum([int(el) for el in num])
    while num > text_len:
        num -= text_len
    new_text += text[num]
    text[num] = "delete"
    text.remove("delete")
print(new_text)