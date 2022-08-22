from exam_4.appliances.fridge import Fridge
from exam_4.appliances.laptop import Laptop
from exam_4.appliances.tv import TV
from exam_4.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.children.extend(children)
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.calculate_expenses(self.appliances, self.children)


