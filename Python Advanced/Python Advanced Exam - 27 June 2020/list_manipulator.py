def add(n_list, data):
    if data[0] == "beginning":
        for el in data[:0:-1]:
            n_list.insert(0, el)
    else:
        for el in data[1:]:
            n_list.append(el)
    return n_list


def remove(n_list, data):
    if data[0] == "beginning":
        if len(data) > 1:
            num = data[1]
            if num == 1:
                num = 2
            n_list = n_list[num:]
        else:
            n_list = n_list[1:]
    else:
        if len(data) > 1:
            num = data[1] * -1
            n_list = n_list[:num]
        else:
            n_list = n_list[:-1]
    return n_list


def list_manipulator(*args):
    result = ''
    n_list = list(args[0])
    command = args[1]
    data = args[2:]
    if command == "add":
        result = add(n_list, data)
    if command == "remove":
        result = remove(n_list, data)
    return result


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
