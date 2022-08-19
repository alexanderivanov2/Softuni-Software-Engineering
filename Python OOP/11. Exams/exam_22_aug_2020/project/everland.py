from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumtions: {total_consumption:.2f}$."

    def pay(self):
        information = []
        rooms_to_remove = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                room.budget -= room.expenses + room.room_cost
                string_one = f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {room.budget:.2f}$ left."
                information.append(string_one)
            else:
                information.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                rooms_to_remove.append(room)
        for room_left in rooms_to_remove:
            self.rooms.remove(room_left)
        return "\n".join(el for el in information)

    def status(self):
        result =  ""
        population = sum([room.members_count for room in self.rooms])
        result  += f"Total Population: {sum(population)}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                count = 0
                for c in room.children:
                    result += f"--- Child {count} monthly cost: {c.cost * 30:.2f}$\n"
            if hasattr(room, "appliances"):
                total_expenses = sum([a.get_monthly_expenses() for a in room.appliances])
                result += f"--- Appliances monthly cost: {room.expenses:.2f}$\n"
        return "\n".join(result)

