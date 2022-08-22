from exam_3.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    DECORATION_TYPE = "Plant"

    def __init__(self):
        super().__init__(5, 10)
