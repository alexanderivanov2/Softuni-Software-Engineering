width_apartment = int(input())
length_apartment = int(input())
high_apartment = int(input())

apartment_cubic_spaces = width_apartment * length_apartment * high_apartment
place_get = 0

command = input()

while command != "Done":
    command = int(command)
    place_get += command
    if place_get > apartment_cubic_spaces:
        print(f"No more free space! You need {place_get - apartment_cubic_spaces} Cubic meters more.")
        exit()
    command = input()

print(f"{apartment_cubic_spaces - place_get} Cubic meters left.")