def get_index(degree):
    if degree in range(10, 19):
        return 0
    elif degree in range(19, 25):
        return 1
    else:
        return 2


degrees = int(input())
part_of_day = input()
morning = ["Sweatshirt and Sneakers", "Shirt and Moccasins", "T-Shirt and Sandals"]
afternoon = ["Shirt and Moccasins", "T-Shirt and Sandals", "Swim Suit and Barefoot"]
evening = "Shirt and Moccasins"
index = get_index(degrees)

if part_of_day == "Morning":
    print(f"It's {degrees} degrees, get your {morning[index]}.")
elif part_of_day == "Afternoon":
    print(f"It's {degrees} degrees, get your {afternoon[index]}.")
else:
    print(f"It's {degrees} degrees, get your {evening}.")
