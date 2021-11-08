n = int(input())
l = int(input())
num1, num2 = 1, 1
num_end = n
end_num = 1
sym1 = ord("a")
sym2 = ord("a")
last_char = sym1 + l

while not (num1 == n == num2 and sym1 + 2 == last_char == sym2 + 2):
    while not end_num == num_end:
        end_num += 1
        print(f"{num1}{num2}{chr(sym1)}{chr(sym2)}{end_num}", end=" ")
    if sym1 != last_char:
        sym2 += 1
        if sym2 == last_char:
            sym1 += 1
            if l == 1 and num1 == n == num2 and end_num == num_end:
                break
            sym2 = ord("a")