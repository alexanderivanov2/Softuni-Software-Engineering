def validate_password(password):
    unfulfilled = []
    if not 6 <= len(password) <= 10:
        unfulfilled.append("Password must be between 6 and 10 characters")
    other_symbols = [el for el in password if not (el.isnumeric() or el.isalpha())]
    if other_symbols:
        unfulfilled.append("Password must consist only of letters and digits")
    digit_symbols = [el for el in password if el.isnumeric()]
    if not len(digit_symbols) > 1:
        unfulfilled.append("Password must have at least 2 digits")
    if unfulfilled:
        return "\n".join(unfulfilled)
    return "Password is valid"


password = input()
print(validate_password(password))
