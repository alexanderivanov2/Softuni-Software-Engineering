from project_2_demo.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, caffeine, price=PRICE, milliliters=MILLILITERS):
        super().__init__(name, price, milliliters)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
