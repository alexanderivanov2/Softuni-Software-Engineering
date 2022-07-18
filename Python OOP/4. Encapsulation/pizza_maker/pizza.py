class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("The name cannot be an empty string")
        self.__name = name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough):
        if not dough:
            raise ValueError("You should add dough to the pizza")
        self.__dough = dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, toppings_capacity):
        if toppings_capacity <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = toppings_capacity

    def add_topping(self, topping):

        if self.__toppings_capacity <= len(self.toppings):
            raise ValueError("Not enough space for another topping")
        elif topping._Topping__topping_type in self.toppings:
            self.toppings[topping._Topping__topping_type] += self.toppings[topping._Topping__topping_type]
        else:
            self.toppings[topping._Topping__topping_type] = topping._Topping__weight

    def calculate_total_weight(self):
        total_weight = self.__dough.weight
        for topping in self.toppings:
            total_weight += self.toppings[topping]
        return total_weight
