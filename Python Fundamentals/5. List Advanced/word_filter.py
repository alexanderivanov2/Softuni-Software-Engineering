filtred_words = [word for word in input().split() if len(word) % 2 == 0]
print("\n".join(filtred_words))