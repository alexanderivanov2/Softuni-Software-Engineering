import math

from exam_5.software.software import Software


class LightSoftware(Software):

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Light", math.floor(capacity_consumption * 1.5),
                         math.floor(memory_consumption * 0.5))
