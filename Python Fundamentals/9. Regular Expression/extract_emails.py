import re

pattern = r"(^|(?<=\s))(?P<user>([A-Za-z\d]+[\.\-_]?)+)(?P<sep>@)(?P<host>([A-Za-z]+\-?)+\.([A-Za-z]+\-?)+(\.([A-Za-z]+\-?)+)*)"
text = input()

emails = re.finditer(pattern, text)

for email in emails:

    print(email.group())