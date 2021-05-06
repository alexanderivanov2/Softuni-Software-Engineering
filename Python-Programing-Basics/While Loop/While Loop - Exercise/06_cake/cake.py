cake_length = int(input())
cake_width = int(input())
cake_size = cake_width * cake_length
piece = input()

while piece != "STOP":
    cake_size -= int(piece)
    if cake_size < 0:
        print(f"No more cake left! You need {abs(cake_size)} pieces more.")
        exit()

    piece = input()

print(f"{cake_size} pieces are left.")
