n = int(input())
word = input()
collection = []
all_sent = []

for i in range(0, n):
    sentence = input()
    all_sent.append(sentence)
    if word in sentence:
        collection.append(sentence)

print(all_sent)
print(collection)