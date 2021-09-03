years = int(input())
price_wash_machine = float(input())
toys_price = int(input())
saved_money = 0
toy_number = 0
money_for_birthday = 10

for i in range(1, years + 1):
    if i % 2 == 0:
        saved_money += (money_for_birthday -1)
        money_for_birthday += 10
    else:
        toy_number += 1

saved_money += (toy_number * toys_price)

if saved_money >= price_wash_machine:
    print(f"Yes! {saved_money - price_wash_machine:.2f}")
else:
    print(f"No! {price_wash_machine - saved_money:.2f}")