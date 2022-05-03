sub = input()
word = input()

while sub in word:
    word = word.replace(sub, '')

print(word)