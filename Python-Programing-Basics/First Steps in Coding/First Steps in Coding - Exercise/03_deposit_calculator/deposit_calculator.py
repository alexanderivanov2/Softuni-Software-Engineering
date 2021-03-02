deposit_sum = float(input())
deadtime_deposit = int(input())
taxes_procent = float(input())


def calculate_deposit(dep_sum, deadtime, tax_pr):
    price_sum = dep_sum + (deadtime * (dep_sum * (tax_pr / 100) / 12))
    print(price_sum)


calculate_deposit(deposit_sum, deadtime_deposit, taxes_procent)
