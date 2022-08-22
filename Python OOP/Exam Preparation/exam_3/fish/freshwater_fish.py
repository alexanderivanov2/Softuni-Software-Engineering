from exam_3.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    FISH_TYPE = "FreshwaterFish"

    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)

    def eat(self):
        self.size += 3
