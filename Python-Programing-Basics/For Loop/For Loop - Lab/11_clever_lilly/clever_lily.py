lily_age = int(input())
washing_machine_price = float(input())
price_for_toy = int(input())
get_money = 0
toys = 0
money_present = 10

for i in range(1, lily_age + 1):
    if i % 2 == 0:
        get_money += money_present - 1
        money_present += 10
    else:
        toys += 1

savigs = get_money + (toys * price_for_toy)

if savigs >= washing_machine_price:
    print(f"Yes! {savigs - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - savigs:.2f}")
