from exam_3.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    A_TYPE = "SaltwaterAquarium"

    def __init__(self, name):
        super().__init__(name, 25)
