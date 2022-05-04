min_ord = ord(input())
max_ord = ord(input())
text = input()
total_value = 0
for el in text:
    el_ord = ord(el)
    if min_ord < el_ord < max_ord:
        total_value += el_ord

print(total_value)