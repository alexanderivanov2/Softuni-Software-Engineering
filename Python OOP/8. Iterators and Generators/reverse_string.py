def reverse_text(text):
    word = [char for char in text]
    while word:
        yield word.pop()


for char in reverse_text("step"):
    print(char, end="")