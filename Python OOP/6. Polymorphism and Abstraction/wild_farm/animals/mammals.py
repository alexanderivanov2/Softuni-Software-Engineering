from project.animals.animals import Mammal
from project.food import Food, Fruit, Vegetable, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ :
            eaten = food.quantity * 0.10
            self.food_eaten += food.quantity
            self.weight += eaten
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            eaten = food.quantity * 0.40
            self.food_eaten += food.quantity
            self.weight += eaten
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ in ["Meat", "Vegetable"]:
            eaten = food.quantity * 0.30
            self.food_eaten += food.quantity
            self.weight += eaten
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            eaten = food.quantity * 1.00
            self.food_eaten += food.quantity
            self.weight += eaten
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
