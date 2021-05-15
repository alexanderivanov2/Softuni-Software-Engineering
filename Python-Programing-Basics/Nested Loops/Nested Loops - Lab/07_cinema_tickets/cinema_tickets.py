total_tickets = 0
students = 0
standards = 0
kids = 0
tickets = 0

movie = input()

while movie != "Finish":
    movies_sits = int(input())
    sit = input()
    while sit != "End":
        tickets += 1
        if sit == "standard":
            standards += 1
        elif sit == "kid":
            kids += 1
        else:
            students += 1
        if tickets == movies_sits:
            break
        sit = input()

    print(f"{movie} - {tickets /  movies_sits * 100:.2f}% full.")
    total_tickets += tickets
    tickets = 0
    movie = input()

print(f"Total tickets: {total_tickets}")
print(f"{students / total_tickets * 100:.2f}% student tickets.")
print(f"{standards / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids / total_tickets * 100:.2f}% kids tickets.")
