filter_words = input().split(", ")
text = input()

for filter_word in filter_words:
    text = text.replace(filter_word, "*" * len(filter_word))

print(text)