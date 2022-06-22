def numbers_searching(*args):
    start = min(args)
    end = max(args)
    duplicates = []
    result = []
    for n in range(start, end + 1):
        if n not in args:
            result.append(n)
        elif args.count(n) > 1:
            duplicates.append(n)
    duplicates = sorted(duplicates)
    result.append(duplicates)
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
