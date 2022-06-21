def stock_availability(*args):
    boxes = args[0]
    command = args[1]
    if command == "delivery":
        boxes.extend(args[2:])
        return boxes
    if command == "sell":
        if len(args) == 2:
            boxes = boxes[1:]
        elif isinstance(args[2], int):
            boxes = boxes[args[2]:]
        for arg in args[2:]:
            if arg in boxes:
                count = boxes.count(arg)
                for i in range(count):
                    boxes.remove(arg)
    return boxes










print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))