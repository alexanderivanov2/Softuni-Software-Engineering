from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        super().__init__(self.table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if 100 < value or value < 51:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value
