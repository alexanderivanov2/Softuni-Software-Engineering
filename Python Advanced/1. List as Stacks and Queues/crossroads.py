from collections import deque


def crossroad_passing(all_cars, g_duration, w_duration):
    while True:

        car_1 = all_cars.popleft()

        length = len(car_1)

        if length <= g_duration:

            g_duration -= length

            if g_duration == 0:
                return all_cars



        else:

            if g_duration > 0:

                length -= g_duration

                if length <= free_window_duration:

                    return all_cars

                else:

                    length -= free_window_duration

                    print("A crash happened!")

                    print(f"{car_1} was hit at {car_1[-length]}.")

                    exit()

        if not all_cars:
            return all_cars


ENDING = "END"

GO_TO_FUNCTION = "green"

green_light_duration = int(input())

free_window_duration = int(input())

car = input()

cars = deque()

count = 0

while car != ENDING:

    if car == GO_TO_FUNCTION:
        if cars:
            cars = crossroad_passing(cars, green_light_duration, free_window_duration)
    else:

        cars.append(car)

        count += 1

    car = input()

print("Everyone is safe.")

if cars:

    print(f"{count - len(cars)} total cars passed the crossroads.")

else:

    print(f"{count} total cars passed the crossroads.")
