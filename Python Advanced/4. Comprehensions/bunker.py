def create_categories():
    categ = {}
    elements = input().split(", ")
    categ_count = len(elements)
    for el in elements:
        categ[el] = {'items': [], 'quantity': 0, 'quality': 0}
    return categ, categ_count


def fill_categories(categ1):
    n = int(input())
    all_items1 = 0
    all_quality1 = 0
    for i in range(n):
        elem, item, data = input().split(" - ")
        data2 = data.split(";")
        quantity = data2[0].split(":")[1]
        quality = data2[1].split(":")[1]
        categ1[elem]["items"].append(item)
        categ1[elem]["quantity"] += int(quantity)
        categ1[elem]["quality"] += int(quality)
        all_items1 += int(quantity)
        all_quality1 += int(quality)
    return categ1, all_items1, all_quality1


categories, count = create_categories()
categories, all_items, all_quality = fill_categories(categories)
print(f"Count of items: {all_items}")
print(f"Average quality: {all_quality / count:.2f}")
for k, v in categories.items():
    print(f"{k} -> {', '.join(x for x in v['items'])}")
