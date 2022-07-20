class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        elif price > self.__budget:
            return "Not enough budget"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name]
        if not worker:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker[0])
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_pay = sum([w.salary for w in self.workers])
        if total_pay > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_pay
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money = sum([a.money_for_care for a in self.animals])
        if total_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [l for l in self.animals if l.__class__.__name__ == "Tiger"]
        cheetahs = [l for l in self.animals if l.__class__.__name__ == "Cheetah"]
        l_str = '\n'.join(f"{l}" for l in lions)
        t_str = "\n".join(f"{t}" for t in tigers)
        c_str = "\n".join(f"{c}" for c in cheetahs)
        return f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n{l_str}\n" \
               f"----- {len(tigers)} Tigers:\n{t_str}\n----- {len(cheetahs)} Cheetahs:\n{c_str}"

    def workers_status(self):
        keepers = [l for l in self.workers if l.__class__.__name__ == "Keeper"]
        caretakers = [l for l in self.workers if l.__class__.__name__ == "Caretaker"]
        vets = [l for l in self.workers if l.__class__.__name__ == "Vet"]
        l_str = '\n'.join(f"{l}" for l in keepers)
        t_str = "\n".join(f"{t}" for t in caretakers)
        c_str = "\n".join(f"{c}" for c in vets)
        return f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n{l_str}\n" \
               f"----- {len(caretakers)} Caretakers:\n{t_str}\n----- {len(vets)} Vets:\n{c_str}"
