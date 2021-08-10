budget = float(input())
tickets = input().lower()
fans = int(input())

normal_ticket = 249.99 * fans
vip_ticket = 499.99 * fans

if fans <= 4:
    budget -= budget * 0.75
elif fans <= 9:
    budget -= budget * 0.6
elif fans <= 24:
    budget -= budget * 0.5
elif fans <= 49:
    budget -= budget * 0.4
else:
    budget -= budget * 0.25

if tickets == "normal":
    if budget >= normal_ticket:
        print(f"Yes! You have {budget-normal_ticket:.2f} leva left.")
    else:
        print(f"Not enough money! You need {normal_ticket - budget:.2f} leva.")
else:
    if budget >= vip_ticket:
        print(f"Yes! You have {budget - vip_ticket:.2f} leva left.")
    else:
        print(f"Not enough money! You need {vip_ticket - budget:.2f} leva.")