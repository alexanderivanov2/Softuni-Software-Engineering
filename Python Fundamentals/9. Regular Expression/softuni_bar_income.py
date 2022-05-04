import re

pattern = r"%(?P<name>[A-Z][a-z]+)\%[^\$\|\%\.\d]*<(?P<product>\w+)\>[^\$\|\%\.\d]*\|(?P<quantity>\d+)\|[^\$\|\%\.\d]*(?P<price>\d+\.?\d*)\$"
total_income = 0

txt = input()

while not txt == 'end of shift':
    buyer = re.match(pattern, txt)
    if buyer:
        total_price = int(buyer.group("quantity")) * float(buyer.group("price"))
        print(f"{buyer.group('name')}: {buyer.group('product')} - {total_price:.2f}")
        total_income += total_price
    txt = input()

print(f"Total income: {total_income:.2f}")