text = [word for word in input().split() if word == word[::-1]]
search = input()

print(text)
print(f"Found palindrome {text.count(search)} times")
