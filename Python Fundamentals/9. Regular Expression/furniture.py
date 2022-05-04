import re

pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+(\.?\d+)?)\!(?P<quantitiy>\d+)"
bought_furniture = []
total_cost = 0

txt = input()

while not txt == "Purchase":
    action = re.match(pattern, txt, re.IGNORECASE)
    if action:
        el_dict = action.groupdict()
        bought_furniture.append(el_dict["name"])
        total_cost += float(el_dict["price"]) * int(el_dict['quantitiy'])
    txt = input()

print("Bought furniture:")
if bought_furniture:
    print("\n".join(bought_furniture))
print(f"Total money spend: {total_cost:.2f}")
