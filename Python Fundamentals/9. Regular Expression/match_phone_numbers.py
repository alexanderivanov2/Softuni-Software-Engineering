import re

txt = input()
regex_pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"

find_all_matches = re.findall(regex_pattern, txt)

print(", ".join(find_all_matches))