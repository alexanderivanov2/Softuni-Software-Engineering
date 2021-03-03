CAKE = 45
GOFRET = 5.80
PANCAKE = 3.20

number_days = int(input())
numbers_of_bakers = int(input())
number_of_cake_per_day = int(input())
number_of_gofrets_per_day = int(input())
number_of_pancakes_per_day = int(input())


def calculate_sum_for_charity(days, bakers, cakes, gofrets, pancakes, price_cake, price_gofrets, price_pancakes):
    cakes_profit = (days * (cakes * bakers)) * price_cake
    gofrets_profit = (days * (gofrets * bakers)) * price_gofrets
    pancakes_profit = (days * (pancakes * bakers)) * price_pancakes
    profit = cakes_profit + gofrets_profit + pancakes_profit
    final_profit = profit - (profit / 8)
    print(round(final_profit, 2))


calculate_sum_for_charity(number_days, numbers_of_bakers, number_of_cake_per_day, number_of_gofrets_per_day,
                          number_of_pancakes_per_day, CAKE, GOFRET, PANCAKE)
