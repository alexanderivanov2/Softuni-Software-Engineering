class Vehicle:

    def __init__(self, type: str, model: str, price: int, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def change(self, money):
        change = money - self.price
        return change

    def buy(self, money, owner):
        if money < self.price:
            return "Sorry, not enough money"
        elif self.owner:
            return "Car already sold"
        self.owner = owner
        return f"Successfully bought a {self.type}. Change: {self.change(money):.2f}"

    def sell(self):
        if not self.owner:
            return "Vehicle has no owner"
        self.owner = None

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)