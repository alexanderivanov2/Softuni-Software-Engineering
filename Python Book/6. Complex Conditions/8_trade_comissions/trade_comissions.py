city = input().title()
s = float(input())  #number of sales

comission = 0
error = "error"

if city == "Sofia":
    if 0 <= s <= 500:
        comission += s * 0.05
    elif 500 < s <= 1000:
        comission += s * 0.07
    elif 1000 < s <= 10000:
        comission += s * 0.08
    elif s > 10000:
        comission += s * 0.12
    else:
        print("error")
elif city == "Varna":
    if 0 <= s <= 500:
        comission += s * 0.045
    elif 500 < s <= 1000:
        comission += s * 0.075
    elif 1000 < s <= 10000:
        comission += s * 0.10
    elif s > 10000:
        comission += s * 0.13
    elif s < 0:
        error = "error"
elif city == "Plovdiv":
    if 0 <= s <= 500:
        comission += s * 0.055
    elif 500 < s <= 1000:
        comission += s * 0.08
    elif 1000 < s <= 10000:
        comission += s * 0.12
    elif s > 10000:
        comission += s * 0.145
    else:
        print(error)
else:
    print("error")

if comission > 0:
    print(f"{comission:.2f}")