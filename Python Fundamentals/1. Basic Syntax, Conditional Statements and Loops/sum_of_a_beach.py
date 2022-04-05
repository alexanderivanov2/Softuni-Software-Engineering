text = input().lower()
words = ["sand", "water", "fish", "sun"]
counter = 0

for word in words:
    repeat = text.count(word)
    if repeat > 0:
        counter += repeat

print(counter)