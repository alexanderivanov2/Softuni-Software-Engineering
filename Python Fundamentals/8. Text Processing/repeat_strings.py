words = input().split()

for word in words:
    print(f"{word * len(word)}", end="")
