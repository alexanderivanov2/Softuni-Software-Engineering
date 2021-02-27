dogs_num = int(input())
other_animals_num = int(input())


def price_food_animals(dogs, other_animals):
    price = dogs * 2.50 + other_animals * 4
    return price


price_all = price_food_animals(dogs_num, other_animals_num)
print(f"{price_all} lv.")
