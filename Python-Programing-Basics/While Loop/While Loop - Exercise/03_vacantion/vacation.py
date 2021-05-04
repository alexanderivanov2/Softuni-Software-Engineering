need_money = float(input())
money_saves = float(input())
spend_counter = 0
days = 0
while money_saves < need_money:
    days += 1
    operation = input()
    money = float(input())
    if operation == "spend":
        spend_counter += 1
        if spend_counter == 5:
            print(f"You can't save the money.\n{days}")
            exit()
        if money > money_saves:
            money_saves = 0
        else:
            money_saves -= money
    else:
        spend_counter = 0
        money_saves += money

print(f"You saved the money for {days} days.")
