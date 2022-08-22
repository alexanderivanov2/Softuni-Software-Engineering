from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    DECORATION_TYPE = "Base"

    @abstractmethod
    def __init__(self, comfort, price):
        self.comfort = comfort
        self.price = price
