import re

pattern = r"(^|(?<=\s))_(?P<variable_name>[a-zA-Z\d]+)($|(?=\s))"
text = input()

variables = re.findall(pattern, text)
print(','.join([el[1] for el in variables]))