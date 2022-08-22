class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        consumption = 0
        for r in self.rooms:
            consumption += r.expenses + r.room_cost
        return f"Monthly consumption: {consumption:.2f}$."

    def pay(self):
        information = []
        rooms_remove = []
        for r in self.rooms:
            expenses = r.expenses + r.room_cost
            if r.budget >= expenses:
                r.budget -= expenses
                information.append(f"{r.family_name} paid {expenses:.2f}$ and have {r.budget:.2f}$ left.")
            else:
                information.append(f"{r.family_name} does not have enough budget and must leave the hotel.")
                rooms_remove.append(r)
            [self.rooms.remove(r) for r in rooms_remove]
        return "\n".join(inf for inf in information)

    def status(self):
        message = f"Total population: {sum([r.members_count for r in self.rooms])}\n"
        for r in self.rooms:
            message += f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$\n"
            if r.children:
                for c in r.children:
                    message += f"--- Child {r.children.index(c) + 1} monthly cost: {c.get_monthly_expense():.2f}$\n"
            if hasattr(r, "appliances"):
                total = sum([a.get_monthly_expense() for a in r.appliances])
                message += f"--- Appliances monthly cost: {total:.2f}$\n"

        return message


