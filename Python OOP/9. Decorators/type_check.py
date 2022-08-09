def type_check(type_variable):
    def decorator(func):
        def wrapper(argument):
            if isinstance(argument, type_variable):
                return func(argument)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2("Not A Number"))

