from exam_4.appliances.fridge import Fridge
from exam_4.appliances.laptop import Laptop
from exam_4.appliances.tv import TV
from exam_4.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name,salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        self.calculate_expenses(self.appliances)

