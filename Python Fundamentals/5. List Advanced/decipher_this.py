text = input().split()
decipher = []
for word in text:
    char = chr(int(''.join(el for el in word if el.isdigit())))
    decipher_word = [el for el in word if el.isalpha()]
    decipher_word.insert(0, char)
    decipher_word[1], decipher_word[-1] = decipher_word[-1], decipher_word[1]
    decipher.append(''.join(decipher_word))

print(*decipher)
