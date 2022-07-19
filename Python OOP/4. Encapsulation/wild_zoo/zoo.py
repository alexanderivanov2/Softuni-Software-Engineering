class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, budget):
        self.__budget = budget

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, animal_capacity):
        self.__animal_capacity = animal_capacity

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, workers_capacity):
        self.__workers_capacity = workers_capacity

    def find_worker_in_zoo(self, workers, worker_name):
        for worker in workers:
            if worker.name == worker_name:
                return worker

    def calculate_money_for_pay(self, workers):
        need_money = 0
        for worker in workers:
            need_money += worker.salary
        return need_money

    def calculate_money_for_care(self, animals):
        need_money = 0
        for animal in animals:
            need_money += animal.money_for_care
        return need_money

    def get_type_animals(self, animals):
        dict_animals = {"Lion": [], "Tiger": [], "Cheetah": []}
        for animal in animals:
            dict_animals[animal.__class__.__name__].append(animal)
        return dict_animals

    def get_type_workers(self, workers):
        dict_workers = {'Keeper': [], 'Caretaker': [], 'Vet': []}
        for worker in workers:
            dict_workers[worker.__class__.__name__].append(worker)
        return dict_workers

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = self.find_worker_in_zoo(self.workers, worker_name)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        need_money = self.calculate_money_for_pay(self.workers)
        if need_money > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= need_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        need_money = self.calculate_money_for_care(self.animals)
        if need_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= need_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_dict = self.get_type_animals(self.animals)
        title = f"You have {len(self.animals)} animals\n"
        lions = f"----- {len(animals_dict['Lion'])} Lions:\n"
        lions += '\n'.join(str(value) for value in animals_dict["Lion"])
        tigers = f"----- {len(animals_dict['Tiger'])} Tigers:\n"
        tigers += '\n'.join(str(value) for value in animals_dict["Tiger"])
        cheetahs = f"----- {len(animals_dict['Cheetah'])} Cheetahs:\n"
        cheetahs += '\n'.join(str(value) for value in animals_dict["Cheetah"])
        return title + lions + '\n' + tigers + "\n" + cheetahs

    def workers_status(self):
        workers_dict = self.get_type_workers(self.workers)
        title = f"You have {len(self.workers)} workers\n"
        keepers = f"----- {len(workers_dict['Keeper'])} Keepers:\n"
        keepers += '\n'.join(str(value) for value in workers_dict['Keeper'])
        caretakers = f"----- {len(workers_dict['Caretaker'])} Caretakers:\n"
        caretakers += '\n'.join(str(value) for value in workers_dict['Caretaker'])
        vet = f"----- {len(workers_dict['Vet'])} Vets:\n"
        vet += '\n'.join(str(value) for value in workers_dict['Vet'])
        return title + keepers + "\n" + caretakers + '\n' + vet
