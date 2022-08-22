import math

from exam_5.hardware.hardware import Hardware


class PowerHardware(Hardware):

    def __init__(self, name, capacity, memory):
        super().__init__(name,"Power", math.floor(capacity * 0.25), math.floor(memory * 1.75))