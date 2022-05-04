import re

pattern = r"(?P<sub_domain>www\.)(?P<domain>([A-Za-z\d]+\-?)+)(?P<domain_extension>(\.[a-z]+)+)"

text = input()
domains = []
while text:
    search_domain = re.finditer(pattern, text)
    if search_domain:
        for domain in search_domain:
            print(domain.group())
    text = input()

