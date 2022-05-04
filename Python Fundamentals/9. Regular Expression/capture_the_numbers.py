import re

pattern = r"\d+"
numbers = []
text = input()

while text:
    numbers.extend(re.findall(pattern, text))
    text = input()

print(" ".join(numbers))