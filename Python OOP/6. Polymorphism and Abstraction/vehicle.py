from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Truck(Vehicle):
    def drive(self, distance):
        need_fuel = (self.fuel_consumption + 1.6) * distance
        if need_fuel <= self.fuel_quantity:
            self.fuel_quantity -= need_fuel

    def refuel(self, fuel):
        self.fuel_quantity += (fuel - fuel * 0.05)


class Car(Vehicle):
    def drive(self, distance):
        need_fuel = (self.fuel_consumption + 0.9) * distance
        if need_fuel <= self.fuel_quantity:
            self.fuel_quantity -= need_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
print(car.fuel_quantity)
print(car.fuel_consumption)
print(truck.fuel_quantity)
print(truck.fuel_consumption)