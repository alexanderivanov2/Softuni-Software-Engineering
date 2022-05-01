n = int(input())
word_synonym_dict = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in word_synonym_dict:
        word_synonym_dict[word] = []
    word_synonym_dict[word].append(synonym)

[print(f"{key} - {', '.join(value)}") for key, value in word_synonym_dict.items()]