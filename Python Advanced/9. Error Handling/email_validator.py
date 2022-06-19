class NameTooShortError(Exception):
    """Name Must be more than 4 characters"""


class MustContainAtSymbolError(Exception):
    """Email must contain @"""


class InvalidDomainError(Exception):
    """"Domain must be one of the following: .com, .bg, .org, .net"""


email = input()
domains = [".com", ".bg", ".org", ".net"]
while not email == "END":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    name, second_part = email.split("@")
    if len(name) < 5:
        raise NameTooShortError("Name must be more than 4 characters")
    domain = f".{second_part.split('.')[1]}"
    if domain not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")
    email = input()