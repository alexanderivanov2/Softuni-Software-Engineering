budget = float(input())
statist_count = int(input())
price_for_cloth = float(input())

price_of_decor = budget * 0.10
price_for_cloth *= statist_count

if statist_count > 150:
    price_for_cloth -= price_for_cloth * 0.10

need_budget = price_for_cloth + price_of_decor

if budget >= need_budget:
    print(f"Action!\nWingard starts filming with {budget - need_budget:.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {need_budget - budget:.2f} leva more.")
