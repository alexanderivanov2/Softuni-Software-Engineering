price_strawberry = float(input())
bananas_weight = float(input())
orange_weight = float(input())
raspberries_weight = float(input())
strawberry_weight = float(input())


def calculate_bill(strawberry_p, banana_kg, orange_kg, raspberries_kg, strawberry_kg):
    raspberries_price = strawberry_p / 2
    orange_price = raspberries_price - (raspberries_price * 0.40)
    banana_price = raspberries_price - (raspberries_price * 0.80)
    bill = (strawberry_p * strawberry_kg) + (raspberries_price * raspberries_kg) + (orange_price * orange_kg) + (
                banana_price * banana_kg)
    print(bill)


calculate_bill(price_strawberry, bananas_weight, orange_weight, raspberries_weight, strawberry_weight)
