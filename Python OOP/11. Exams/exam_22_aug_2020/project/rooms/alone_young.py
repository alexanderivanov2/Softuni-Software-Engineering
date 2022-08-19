from project.rooms.room import Room
from project.appliances.tv import TV

class AloneYoung(Room):
    def __init__(self, family_name, budget):
        super().__init__(family_name, budget, 1)
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)

