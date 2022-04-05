def action_out_of_stock(gifts, gift):
    gifts = [el if el != gift else None for el in gifts]
    return gifts


def action_required(gifts, gift, index):
    gifts[index] = gift
    return gifts


def action_just_in_case(gifts, gift):
    gifts[-1] = gift
    return gifts


gifts = [el for el in input().split()]

command = input()

while not command == "No Money":
    command, gift, *index = command.split()
    if command == "OutOfStock":
        gifts = action_out_of_stock(gifts, gift)
    elif command == "Required" and 0 <= int(index[0]) < len(gifts):
        gifts = action_required(gifts, gift, int(index[0]))
    elif command == "JustInCase":
        gifts = action_just_in_case(gifts, gift)
    command = input()

print(' '.join(el for el in gifts if not el == None))
