products = {}
total_products = 0
total_quantity = 0
command = input()

while not command == 'statistics':
    product, quantity = command.split(":")
    quantity = int(quantity)
    if product not in products:
        products[product] = quantity
        total_products += 1
    else:
        products[product] += quantity
    total_quantity += quantity
    command = input()

print("Products in stock:")
print('\n'.join(f'- {key}: {value}' for key, value in products.items()))
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")