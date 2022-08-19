from project.people.child import Child


class Room:
    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_cost = 0
        for arg_one in args:
            for arg in arg_one:
                if isinstance(arg, Child):
                    total_cost += arg.cost * 30
                else:
                    total_cost += arg.get_monthly_expense()
        self.expenses = total_cost
