year = int(input())

while True:
    year += 1
    if len(set([int(el) for el in str(year)])) == len(str(year)):
        print(year)
        break
