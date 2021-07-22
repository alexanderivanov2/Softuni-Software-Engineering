a = int(input())

range = (a >= 100 and a <= 200) or a == 0

if not range:
    print("invalid")