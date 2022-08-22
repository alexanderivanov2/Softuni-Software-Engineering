from exam_4.appliances.fridge import Fridge
from exam_4.appliances.stove import Stove
from exam_4.appliances.tv import TV
from exam_4.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]
        self.calculate_expenses(self.appliances)
