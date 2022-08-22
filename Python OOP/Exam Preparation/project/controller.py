from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    cars = []
    drivers = []
    races = []



    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in ["MuscleCar", "SportsCar"]:
            search_car = [c for c in self.cars if c.model == model and c]
            if search_car:
                raise Exception(f"Car {model} is already created!")

            car = MuscleCar(model, speed_limit) if car_type == "MuscleCar" else SportsCar(model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        search_driver = [d for d in self.drivers if d.name == driver_name]
        if search_driver:
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        search_race = [r for r in self.races if r.name == race_name]
        if search_race:
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = [d for d in self.drivers if d.name == driver_name]
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = [c for c in self.cars if c.type_of_car == car_type and not c.is_taken]
        if not car:
            raise Exception(f"Car {car_type} could not be found!")
        car_for_add = car[-1]
        car_for_add.is_taken = True
        driver = driver[0]
        if driver.car:
            old_model = driver.car.model
            driver.car.is_taken = False
            driver.car = car_for_add
            new_model = car_for_add.model
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."
        driver.car = car_for_add
        return f"Driver {driver_name} chose the car {car_for_add.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        search_race = [r for r in self.races if r.name == race_name]
        if not search_race:
            raise Exception(f"Race {race_name} could not be found!")
        driver = [d for d in self.drivers if d.name == driver_name]
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        race = search_race[0]
        driver = driver[0]
        in_drivers = [d for d in race.drivers if d.name == driver.name]
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if in_drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name]
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        race = race[0]
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        race_drivers = race.drivers
        race_rankings = sorted(race_drivers, key=lambda x: -x.car.speed_limit)
        message = []
        for r in race_rankings[0:3]:
            r.number_of_wins += 1
            txt = f"Driver {r.name} wins the {race_name} race with a speed of {r.car.speed_limit}."
            message.append(txt)
        return "\n".join(message)
#
# controller = Controller()
# print(controller.create_driver("Peter"))
# print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("SportsCar", "Porsche 911", 580))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
# print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
# print(controller.create_driver("John"))
# print(controller.create_driver("Jack"))
# print(controller.create_driver("Kelly"))
# print(controller.add_car_to_driver("Kelly", "MuscleCar"))
# print(controller.add_car_to_driver("Jack", "MuscleCar"))
# print(controller.add_car_to_driver("John", "SportsCar"))
# print(controller.create_race("Christmas Top Racers"))
# print(controller.add_driver_to_race("Christmas Top Racers", "John"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
# print(controller.start_race("Christmas Top Racers"))
# [print(d.name, d.number_of_wins) for d in controller.drivers]
