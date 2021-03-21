PUZZLE = 2.60
TALKING_DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2

vacation_price = float(input())
puzzle_number = int(input())
talking_doll_number = int(input())
teddy_bear_number = int(input())
minions_number = int(input())
truck_number = int(input())

count_of_buys = puzzle_number + truck_number + talking_doll_number + teddy_bear_number + minions_number
price_of_all_toys = puzzle_number * PUZZLE + talking_doll_number * TALKING_DOLL + teddy_bear_number * TEDDY_BEAR + \
                    minions_number * MINION + truck_number * TRUCK

if count_of_buys >= 50:
    price_of_all_toys -= price_of_all_toys * 0.25

price_of_all_toys -= price_of_all_toys * 0.10

if vacation_price <= price_of_all_toys:
    print(f"Yes! {price_of_all_toys - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - price_of_all_toys:.2f} lv needed.")
