heritage = float(input())
end_year = int(input())
years = 17
spent_money_even = 0
spent_money_odd = 0

for i in range(1800, end_year + 1):
    years += 1
    if i % 2 == 0:
        spent_money_even += 12000
    else:
        spent_money_odd += 12000 + 50 * years

    if spent_money_even + spent_money_odd <= heritage:
        print(f"Yes! He will live a carefree life and will have {heritage - (spent_money_even + spent_money_odd):.2f} "
              f"dollars left.")
    else:
        print(f"He will need {(spent_money_odd + spent_money_even) - heritage:.2f} dollars to survive.")