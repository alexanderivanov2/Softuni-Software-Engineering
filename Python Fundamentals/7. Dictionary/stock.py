list_products = input().split()
products = {}
searched_products = input().split()

for i in range(0, len(list_products), 2):
    products[list_products[i]] = int(list_products[i + 1])

for product in searched_products:
    if product not in products:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {products[product]} of {product} left")