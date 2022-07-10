class Person:
    def __init__(self, name):
        self.name = name

    def get_attributes_with_prefix(self, prefix):
        return [key for (key) in self.__dict__.keys() if key.startswith(prefix)]

    def set_later_value(self):
        self.age = 17

    def set_dict_value(self):
        self.__dict__['something'] = 5

    def __repr__(self):
        return '; '.join(
            [f"{key} = {value}" for (key, value) in self.__dict__.items()])


pesho = Person('Pesho')
pesho.set_later_value()
example = str(pesho)
print(example)
del pesho.age
print(pesho.__dict__)
print(pesho.get_attributes_with_prefix('name'))
pesho.name_lower = 'second'
print(pesho.get_attributes_with_prefix('name'))
pesho.set_dict_value()
print(pesho)
print(pesho.__dict__)
print(pesho.__dict__['something'])
print(pesho.something)
print(Person.__dict__)
print(getattr(Person, 'set_dict_value'))