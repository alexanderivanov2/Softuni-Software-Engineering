def list_manipulator(*args):
    numbers = args[0]
    action = args[1]
    direction = args[2]
    if action == "add":
        if direction == "beginning":
            numbers = list(args[3:]) + numbers
        else:
            numbers += list(args[3:])
    elif action == "remove":
        if direction == "end":
            if len(args) == 3:
                numbers.pop()
            else:
                for i in range(args[3]):
                    numbers.pop()
        elif direction == "beginning":
            if len(args) == 3:
                numbers.pop(0)
            else:
                for i in range(args[3]):
                    numbers.pop(0)
    return numbers




print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))