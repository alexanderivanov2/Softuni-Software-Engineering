def check_index(targets_pr, index_pr):
    if 0 <= index_pr < len(targets_pr):
        return True
    return False


def in_range(targets_pr, index_pr, data_pr):
    if 0 <= index_pr - data_pr and index_pr + data_pr < len(targets_pr):
        return True
    return False


def make_shot(targets_pr, index_pr, data_pr):
    if targets_pr[index_pr] - data_pr <= 0:
        targets_pr.pop(index_pr)
        return targets_pr
    targets_pr[index_pr] -= data_pr
    return targets_pr


def insert_target(targets_pr, index_pr, data_pr):
    targets_pr.insert(index_pr, data_pr)
    return targets_pr


def do_strike(targets_pr, index_pr, data_pr):
    fisrt_part = targets_pr[:index_pr - data_pr]
    second_part = targets_pr[index_pr + data_pr + 1:]
    return fisrt_part + second_part


targets = [int(target) for target in input().split()]

command = input()

while not command == "End":
    action, *data = command.split()
    index = int(data[0])
    data = int(data[1])
    is_index = check_index(targets, index)
    if action == "Shoot" and is_index:
        targets = make_shot(targets, index, data)
    elif action == "Add":
        if is_index:
            targets = insert_target(targets, index, data)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if is_index and in_range(targets, index, data):
            targets = do_strike(targets, index, data)
        else:
            print("Strike missed!")
    command = input()

print("|".join(str(el) for el in targets))
