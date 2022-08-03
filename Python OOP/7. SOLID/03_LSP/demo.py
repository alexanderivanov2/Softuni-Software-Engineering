from abc import abstractmethod, ABC


class Duck:
    def __init__(self, size, color):
        self.size = size
        self.color = color


class LiveDuck(Duck, ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class FakeDuck(Duck, ABC):
    pass


class RubberDuck(FakeDuck):
    pass


class RobotDuck(FakeDuck):
    def __init__(self, size, color, energy):
        self.super().__init__(size, color)
        self.batery_energy = energy

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0
