from collections import deque


def find_purennes(list_n):
    result = 0
    for i in range(len(list_n)):
        result += list_n[i] * i
    return result


def best_list_pureness(*args):
    list_n = deque(args[0])
    k = args[1]
    rotation = 0
    max_pureness = 0
    for i in range(k + 1):
        pureness = find_purennes(list_n)
        if pureness > max_pureness:
            max_pureness = pureness
            rotation = i
        element = list_n.pop()
        list_n.appendleft(element)
    return f"Best pureness {max_pureness} after {rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)