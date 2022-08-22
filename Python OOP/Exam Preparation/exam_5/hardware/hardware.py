class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.current_capacity = 0
        self.current_memory = 0

    def install(self, software):
        if self.current_capacity + software.capacity_consumption <= self.capacity and self.current_memory + software.memory_consumption <= self.memory:
            self.software_components.append(software)
            self.current_memory += software.memory_consumption
            self.current_capacity += software.capacity_consumption
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.current_memory -= software.memory_consumption
            self.current_capacity -= software.capacity_consumption
            self.software_components.remove(software)
