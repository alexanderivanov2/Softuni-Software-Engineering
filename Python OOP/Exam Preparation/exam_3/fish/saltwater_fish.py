from exam_3.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    FISH_TYPE = "SaltwaterFish"

    def __init__(self, name, species, price):
        super().__init__(name, species, 5, price)

    def eat(self):
        self.size += 2
