word_one = input()
word_two = input()

for i in range(len(word_one)):
    if word_one[i] == word_two[i]:
        continue
    else:
        word_one = [el for el in word_one]
        word_one[i] = word_two[i]
        word_one = ''.join(word_one)
        print(word_one)
