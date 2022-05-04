import re

regex_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
txt = input()
all_matches = re.findall(regex_pattern, txt)

print(" ".join(all_matches))