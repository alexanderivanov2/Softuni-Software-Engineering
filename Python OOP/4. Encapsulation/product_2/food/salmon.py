from project_2_demo.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price, grams=GRAMS):
        super().__init__(name, price, grams)
