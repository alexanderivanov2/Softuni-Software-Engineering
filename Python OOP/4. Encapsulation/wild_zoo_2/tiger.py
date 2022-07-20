from project_wild_zoo_2.animal import Animal

class Tiger(Animal):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 45)