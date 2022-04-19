vowels = ['a', 'o', 'u', 'e', 'i']
no_vowels_word = [el for el in input() if el not in vowels]
print("".join(no_vowels_word))