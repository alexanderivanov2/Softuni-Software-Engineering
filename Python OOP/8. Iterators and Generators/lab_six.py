def reverse_text(txt):
    for i in range(len(txt)-1, -1, -1):
        yield txt[i]

for char in reverse_text("step"):
    print(char, end='')