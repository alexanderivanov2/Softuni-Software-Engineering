yard_sq_m = float(input())


def calculation_expenses(yard):
    price_yard = yard * 7.61
    discount = price_yard * 0.18
    print(f"The final price is: {price_yard - discount} lv.")
    print(f"The discount is: {discount} lv.")


calculation_expenses(yard_sq_m)
