class Person:
    #max_age = 150

    def __init__(self, name, age):
        self.validate_age(age)
        self.name = name
        self.age = age

    @staticmethod
    def validate_age(age):
        if 0 > age or age > Person.max_age:
            raise ValueError("Age is invalid")

    @staticmethod
    def is_age_valid(age):
        return 0 <= age <= Person.max_age

    @classmethod
    def is_age_valid_2(cls, age):
        max_age = getattr(cls, 'max_age', 150)
        return  0 <= age <= max_age

# print(Person('gosho', 11))
# print(Person.is_age_valid(78))
# print(Person('gosho', 1111))
print(Person.is_age_valid_2(5555))
print(Person.is_age_valid_2(5))
print(Person.__dict__)
