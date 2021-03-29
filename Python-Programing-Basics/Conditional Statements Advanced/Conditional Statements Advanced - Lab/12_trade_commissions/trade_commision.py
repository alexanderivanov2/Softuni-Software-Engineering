import math


def get_index_commission(s, maths):
    s = maths.ceil(s)
    if s in range(0, 501):
        return 0
    elif s in range(501, 1001):
        return 1
    elif s in range(1001, 10001):
        return 2
    elif s > 10000:
        return 3


city = input()
sales = float(input())
Sofia = [0.05, 0.07, 0.08, 0.12]
Varna = [0.045, 0.075, 0.1, 0.13]
Plovdiv = [0.055, 0.08, 0.12, 0.145]

index = get_index_commission(sales, math)

if city == "Sofia" and not sales < 0:
    commission = sales * Sofia[index]
    print(f"{commission:.2f}")
elif city == "Varna" and not sales < 0:
    commission = sales * Varna[index]
    print(f"{commission:.2f}")
elif city == "Plovdiv" and not sales < 0:
    commission = sales * Plovdiv[index]
    print(f"{commission:.2f}")
else:
    print("error")
