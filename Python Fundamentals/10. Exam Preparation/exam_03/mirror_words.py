import re

pattern = r"(\#|\@)(?P<word_one>[A-Za-z]{3,})\1\1(?P<word_two>[A-Za-z]{3,})\1"
mirror_words = []
txt = input()
counter = 0
counter_pairs = 0
for match in re.finditer(pattern, txt):
    word_one = match.group("word_one")
    word_two = match.group("word_two")
    counter_pairs += 1
    if word_one[::-1] == word_two:
        counter += 1
        mirror_words.append(f"{word_one} <=> {word_two}")

if counter_pairs == 0:
    print("No word pairs found!")
else:
    print(f"{counter_pairs} word pairs found!")

if counter == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))
