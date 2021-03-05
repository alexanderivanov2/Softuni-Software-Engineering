length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
procent_get = float(input())


def calculate_liters_water(length, width, height, procent):
    aquarium_qb = ((length * width * height) / 1000)
    liters_water = aquarium_qb - (aquarium_qb * (procent / 100))
    print(liters_water)


calculate_liters_water(length_cm, width_cm, height_cm, procent_get)
