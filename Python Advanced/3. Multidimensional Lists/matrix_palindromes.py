rows, columns = [int(i) for i in input().split()]
letter = ord("a")

for r in range(rows):
    for c in range(columns):
        print(f"{chr(letter)}{chr(letter + c)}{chr(letter)}", end=" ")
    print()
    letter += 1