import math


class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def __repr__(self):
        return '; '.join(f'{key} = {value}' for key, value in self.__dict__.items())


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


def get_values(obj, attr_names):
    return [getattr(obj, attr_name, None) for attr_name in attr_names]


pesho = Person('Pesho', 18, 'Sofia', 'Bulgaria')

attr_name = 'name'
print(get_values(pesho, ['city', 'country']))
print(get_values(pesho, ['name', 'something']))

circle = Circle(4)
print(get_values(circle, ['radius', 'area']))
area_method = get_values(circle, ['area'])[0]
print(area_method)
print(area_method())

print(getattr(circle, 'diameter', None))
print(pesho)
pesho.city = 'Plovdiv'
print(pesho)
setattr(pesho, 'city', "Burgas")
setattr(pesho, 'last name', 'Petrov')
print(pesho)
delattr(pesho, 'last name')
print(pesho)

