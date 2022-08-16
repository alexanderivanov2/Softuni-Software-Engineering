class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if software.capacity_consumption > self.capacity or software.memory_consumption > self.memory:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)
        self.memory -= software.memory_consumption
        self.capacity -= software.capacity_consumption

    def uninstall(self, software):
        if software in self.software_components:
            self.capacity += software.capacity_consumption
            self.memory += software.memory_consumption
            self.software_components.remove(software)

