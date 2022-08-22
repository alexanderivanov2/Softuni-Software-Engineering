import math

from exam_5.hardware.hardware import Hardware


class HeavyHardware(Hardware):

    def __init__(self, name, capacity, memory):
        super().__init__(name, "Heavy", capacity * 2, math.floor(memory * 0.75))
