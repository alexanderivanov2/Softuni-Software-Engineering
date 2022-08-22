from exam_3.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    A_TYPE = "FreshwaterAquarium"

    def __init__(self, name):
        super().__init__(name, 50)
