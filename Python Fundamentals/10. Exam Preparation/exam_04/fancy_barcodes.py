import re

pattern = r"(@#{1,})(?P<name>[A-Z][A-Za-z\d]{4,}[A-Z])(@#{1,})"
n = int(input())

for i in range(n):
    txt = input()
    match = re.match(pattern, txt)
    if match:
        for match in re.finditer(pattern, txt):
            barcode = match.group("name")
            digits = re.findall(r"\d", barcode)
            if len(digits) == 0:
                print(f"Product group: 00")
            else:
                print(f"Product group: {''.join(digits)}")
    else:
        print("Invalid barcode")
