from exam_3.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    DECORATION_TYPE = "Ornament"

    def __init__(self):
        super().__init__(1, 5)
