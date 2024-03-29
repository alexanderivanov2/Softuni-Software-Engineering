from exam_2.baked_food.bread import Bread
from exam_2.baked_food.cake import Cake
from exam_2.drink.tea import Tea
from exam_2.drink.water import Water
from exam_2.table.inside_table import InsideTable
from exam_2.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        searched_food = [f for f in self.food_menu if f.name == name]
        if searched_food:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
        elif food_type == "Cake":
            self.food_menu.append(Cake(name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        searched_drink = [d for d in self.drinks_menu if d.name == name]
        if searched_drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type == "Tea":
            self.drinks_menu.append(Tea(name, portion, brand))
        elif drink_type == "Water":
            self.drinks_menu.append(Water(name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        searched_table = [t for t in self.tables_repository if t.table_number == table_number]
        if searched_table:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == "OutsideTable":
            self.tables_repository.append(OutsideTable(table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            food_not_in_menu = []
            for food_name in args:
                is_found = False
                for food in self.food_menu:
                    if food.name == food_name:
                        table.order_food(food)
                        is_found = True
                        break
                if not is_found:
                    food_not_in_menu.append(food_name)

            result = f"Table {table.table_number} ordered:\n"
            for food in table.food_orders:
                result += f"{repr(food)}\n"
            if food_not_in_menu:
                result += f"{self.name} does not have in the menu:\n"
                for food in food_not_in_menu:
                    result += f"{food}\n"

            return result

        return f"Could not find table {table_number}"

    def order_drink(self, table_number, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            drinks_not_in_menu = []
            for drink_name in args:
                is_found = False
                for drink in self.drinks_menu:
                    if drink.name == drink_name:
                        table.order_drink(drink)
                        is_found = True
                        break
                if not is_found:
                    drinks_not_in_menu.append(drink_name)

            result = f"Table {table.table_number} ordered:\n"
            for drink in table.drink_orders:
                result += f"{repr(drink)}\n"
            if drinks_not_in_menu:
                result += f"{self.name} does not have in the menu:\n"
                for drink in drinks_not_in_menu:
                    result += f"{drink}\n"

            return result

        return f"Could not find table {table_number}"

    def leave_table(self, table_number):
        table = [x for x in self.tables_repository if x.table_number == table_number]
        if table:
            table = table[0]
            bill = table.get_bill()
            table.clear()
            self.total_income += bill
            return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        message = ""
        for t in self.tables_repository:
            message += f"{t.free_table_info()}\n"
        return message

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

#
# bakery = Bakery("A")
# print(bakery.add_table("InsideTable", 2, 5))
# print(bakery.add_food("Cake", "Cake", 2))
# print(bakery.add_drink("Tea", "B", 2, "Black"))
# print(bakery.order_food(2, "Cake", "Cake2"))
# print(bakery.order_drink(2, "A", "B"))
# print(bakery.leave_table(2))
# print(bakery.add_table("InsideTable", 3, 5))
# print(bakery.order_food(3, "Cake", "Cake2"))
# print(bakery.order_drink(3, "A", "B"))
# print(bakery.leave_table(3))
# print(bakery.get_free_tables_info())
# print(bakery.get_total_income())
