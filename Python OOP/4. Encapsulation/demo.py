class Person:
    MIN_AGE = 0
    MAX_AGE = 150

    def __init__(self, first_name, last_name, age, city=None):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age
        self.city = city

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def __validate_name(name):
        if not name:
            raise ValueError("Name cannot be None")
        return True

    # getter
    @property
    def first_name(self):
        return self.__first_name

    # setter
    @first_name.setter
    def first_name(self, new_name):
        if self.__validate_name(new_name):
            self.__first_name = new_name

    def set_age(self, new_age):
        if Person.MIN_AGE <= new_age <= Person.MAX_AGE:
            self.__age = new_age
        else:
            raise ValueError("Not valid age")

    def get_age(self):
        return self.__age
    # def __setattr__(self, key, value):
    #     if key.startswith('_') and len(key) > 1 and key[1] != '_':
    #         key = f"_{self.__class__.__name__}${key}"
    #     return super().__setattr__(key, value)
    #
    # def __getattr__(self, item):
    #     if item.startswith('_') and len(item) > 1 and item[1] != '_':
    #         item = f"_{self.__class__.__name__}${item}"
    #     return super().__getattribute__(item)


pesho = Person('Pesho', 'Petrov', 11)
print(pesho.__dict__)
print(pesho.first_name)
print(pesho.get_age())
# pesho.__age = -1
# pesho.set_age(-1)
# print(pesho.__dict__)
# print(pesho.get_age())
#pesho.name = None
print(pesho.__dict__)
print(pesho.first_name)
print(pesho.full_name)
print(Person._Person__validate_name)