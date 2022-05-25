n = int(input())

cars = set()

for _ in range(n):
    do, number = input().split(", ")
    if do == "IN":
        cars.add(number)
    else:
        cars.remove(number)

if cars:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")
