def oscars_result(num):
    result = ""
    if num == 88:
        result = "Leo finally won the Oscar! Leo is happy"
    elif num == 86:
        result = "Not even for Wolf of Wall Street?!"
    elif num < 88:
        result = "When will you give Leo an Oscar?"
    else:
        result = "Leo got one already!"
    return result


number = int(input())
print(oscars_result(number))
