from project_person_2.person import Person


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
