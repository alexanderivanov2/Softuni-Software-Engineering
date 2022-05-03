def check_length(word):
    if 3 <= len(word) <= 16:
        return True
    return False


def check_for_symbols(word):
    for ch in word:
        if ch.isdigit() or ch.isalpha() or ch == '_' or ch == "-":
            continue
        return False
    return True


txt = input().split(", ")

for el in txt:
    if check_length(el) and check_for_symbols(el):
        print(el)
