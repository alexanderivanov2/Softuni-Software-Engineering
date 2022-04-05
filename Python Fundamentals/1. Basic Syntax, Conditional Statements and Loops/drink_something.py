def get_drink(years):
    result = "drink "
    if years <= 14:
        result += "toddy"
    elif years <= 18:
        result += "coke"
    elif years <= 21:
        result += "beer"
    else:
        result += "whisky"
    return result


print(get_drink(int(input())))
