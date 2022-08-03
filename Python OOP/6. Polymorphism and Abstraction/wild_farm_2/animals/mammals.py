from wild_farm.animals.animal import Mammal
from wild_farm.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Fruit) and not isinstance(food, Vegetable):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.eat(food, 0.10)


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.eat(food, 0.40)


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Meat) and not isinstance(food, Vegetable):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.eat(food, 0.30)


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.eat(food, 1.00)
