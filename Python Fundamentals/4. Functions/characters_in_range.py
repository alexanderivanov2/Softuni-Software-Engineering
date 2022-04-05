def get_characters_between(start, end):
    chars = [chr(el) for el in range(start + 1, end)]
    return " ".join(chars)


start = ord(input())
end = ord(input())

print(get_characters_between(start, end))
