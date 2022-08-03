from abc import ABC, abstractmethod
import time


class AbstractWorker(ABC):
    @abstractmethod
    def work(self):
        raise NotImplementedError()


class EatMixin(ABC):
    @abstractmethod
    def eat(self):
        raise NotImplementedError()

class Workable(AbstractWorker):
    def work(self):
        print("I'm normal worker. I'm working.")


class Eatable(EatMixin):
    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)

class Worker(Workable, Eatable):
    pass





class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):

        self.worker = worker


class WorkManager(Manager):
    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def lunch_break(self):
        self.worker.eat()


class Robot(Workable):
    def work(self):
        print("I'm a robot. I'm working....")


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass


# Може би eat да не е abstracten в бащиния клас. Също може да се създадат два отделни класа, един абстрактен с work и втори наследяващ първия и разширяващ с eat

