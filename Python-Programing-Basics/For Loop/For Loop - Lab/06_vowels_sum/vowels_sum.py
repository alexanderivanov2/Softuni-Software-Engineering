word = input()
vowels = [0, 'a', 'e', 'i', 'o', 'u']
vowels_sum = 0

for ch in word:
    if ch in vowels:
        vowels_sum += vowels.index(ch)

print(vowels_sum)