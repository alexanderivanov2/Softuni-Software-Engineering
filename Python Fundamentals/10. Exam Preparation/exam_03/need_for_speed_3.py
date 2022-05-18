LIMIT_MILEAGE = 100000
MAX_TANK = 75
MIN_MILEAGE = 10000

cars = {}
n = int(input())
for i in range(n):
    car, mileage, fuel = input().split("|")
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

command = input()

while not command == "Stop":
    action, car, *data = command.split(" : ")
    if action == "Drive":
        distance = int(data[0])
        fuel = int(data[1])
        if fuel > cars[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel
            if cars[car]['mileage'] >= LIMIT_MILEAGE:
                del cars[car]
                print(f"Time to sell the {car}!")
    elif action == "Refuel":
        fuel = int(data[0])
        if cars[car]['fuel'] + fuel >= MAX_TANK:
            print(f"{car} refueled with {MAX_TANK - cars[car]['fuel']} liters")
            cars[car]['fuel'] = MAX_TANK
        else:
            cars[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        kilometers = int(data[0])
        if cars[car]['mileage'] - kilometers < MIN_MILEAGE:
            cars[car]['mileage'] = MIN_MILEAGE
        else:
            cars[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()


sorted_cars = dict(sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x)))

for car, value in sorted_cars.items():
    print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")

