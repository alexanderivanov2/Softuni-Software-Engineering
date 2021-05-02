searched_book = input()
checked_book = input()
checks = 0
find = False
while not checked_book == "No More Books":
    if checked_book == searched_book:
        find = True
        break
    checks += 1
    checked_book = input()

if find:
    print(f"You checked {checks} books and found it.")
else:
    print(f"The book you search is not here!\nYou checked {checks} books.")
