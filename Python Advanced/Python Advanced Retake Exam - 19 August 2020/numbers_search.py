def numbers_searching(*args):
    start = min(args)
    end = max(args) + 1
    duplicate = []
    missing = []
    for i in range(start, end):
        if i in args:
            if i in duplicate:
                continue
            else:
                if args.count(i) > 1:
                    duplicate.append(i)
                    continue
        else:
            missing.append(i)
    missing.append(duplicate)
    return missing


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))