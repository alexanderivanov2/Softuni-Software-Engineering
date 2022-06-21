def stock_availability(*args):
    inventory_list = args[0]
    action = args[1]
    data = args[2:]
    if action == "delivery":
        inventory_list.extend(data)
    else:
        if len(data) == 1 and type(data[0]) == int:
            inventory_list = inventory_list[data[0]:]
        elif len(data) > 0:
            for el in data:
                if el in inventory_list:
                    cal_range = inventory_list.count(el)
                    for i in range(cal_range):
                        inventory_list.remove(el)
        else:
            inventory_list = inventory_list[1:]
    return inventory_list



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
