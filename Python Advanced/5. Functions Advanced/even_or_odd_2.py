def even_odd(*args):
    command = args[-1]
    if command == "even":
        return [n for n in args[:-1] if n % 2 == 0]
    else:
        return [n for n in args[:-1] if n % 2 != 0]
