def greeting(name):
    result = "Hello, "
    if name == "Johnny":
        result += "my love!"
    else:
        result += f"{name}!"
    return result


print(greeting(input()))
