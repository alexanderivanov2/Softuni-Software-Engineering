start = int(input())
ending = int(input())
search_number = int(input())
counter = 0
for i in range(start, ending + 1):
    for i2 in range(start, ending + 1):
        counter += 1
        if i + i2 == search_number:
            print(f"Combination N:{counter} ({i} + {i2} = {search_number})")
            exit()

print(f"{counter} combinations - neither equals {search_number}")
