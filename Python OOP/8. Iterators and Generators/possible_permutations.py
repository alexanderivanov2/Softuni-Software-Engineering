from itertools import permutations


def possible_permutations(nums_list):
    perms = permutations(nums_list)
    for perm in perms:
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]