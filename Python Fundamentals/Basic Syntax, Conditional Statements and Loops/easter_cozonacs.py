budget = float(input())
flour_price = float(input())
price_pack_eggs = flour_price * 0.75
price_one_liter_milk = flour_price * 1.25
price_for_one_cozonac = flour_price + price_pack_eggs + (price_one_liter_milk * 0.25)
cozonacs = int(budget // price_for_one_cozonac)
colored_egs = 0
count = 0
count_of_cozonacs = 0
left_money = budget - (price_for_one_cozonac * cozonacs)

for i in range(1, cozonacs + 1):
    colored_egs += 3
    count_of_cozonacs += 1
    count += 1
    if count == 3:
        colored_egs -= (count_of_cozonacs - 2)
        count = 0

print(f"You made {cozonacs} cozonacs! Now you have {colored_egs} eggs and {left_money:.2f}BGN left.")
