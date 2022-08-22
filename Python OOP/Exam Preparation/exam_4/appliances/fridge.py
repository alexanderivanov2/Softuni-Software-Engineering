from exam_4.appliances.appliance import Appliance


class Fridge(Appliance):
    def __init__(self):
        super().__init__(1.2)