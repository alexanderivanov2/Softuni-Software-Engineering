from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [hard for hard in System._hardware if hard.name == hardware_name][0]
        except:
            hardware = []
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        if not hardware:
            return "Hardware does not exist"
        try:
            hardware.install(software)
            System._software.append(software)
        except:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [hard for hard in System._hardware if hard.name == hardware_name][0]
        except:
            hardware = []
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        if not hardware:
            return "Hardware does not exist"
        try:
            hardware.install(software)
            System._software.append(software)
        except:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [hard for hard in System._hardware if hard.name == hardware_name][0]
        except:
            hardware = []
        try:
            software = [soft for soft in System._software if soft.name == software_name][0]
        except:
            software = None
        if not software or not hardware:
            return "Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)


    @staticmethod
    def analyze():
        message = "System Analysis\n"
        message += f"Hardware Components: {len(System._hardware)}\n"
        message += f"Software Components: {len(System._software)}\n"
        hard_mem = 0
        hard_cap = 0
        used_mem = 0
        used_cap = 0
        for hard in System._hardware:
            hard_mem += hard.memory
            hard_cap += hard.capacity
            for soft in hard.software_components:
                used_mem += soft.memory_consumption
                hard_mem += soft.memory_consumption
                used_cap += soft.capacity_consumption
                hard_cap += soft.capacity_consumption

        message += f"Total Operational Memory: {int(used_mem)} / {int(hard_mem)}\n"
        message += f"Total Capacity Taken: {int(used_cap)} / {int(hard_cap)}"
        return message

    @staticmethod
    def system_split():
        message = ""
        for hard in System._hardware:
            message += f"Hardware Component - {hard.name}\n"
            length_es = 0
            length_ls = 0
            memory_usage = 0
            capacity_usage = 0
            soft_comp = []
            for soft in hard.software_components:
                soft_comp.append(soft.name)
                if soft.type == "Light":
                    length_ls += 1
                else:
                    length_es += 1
                memory_usage += soft.memory_consumption
                capacity_usage += soft.capacity_consumption
            total_memory = hard.memory + memory_usage
            total_capacity = hard.capacity + capacity_usage
            message += f"Express Software Components: {length_es}\n"
            message += f"Light Software Components: {length_ls}\n"
            message += f"Memory Usage: {int(memory_usage)} / {int(total_memory)}\n"
            message += f"Capacity Usage: {int(capacity_usage)} / {int(total_capacity)}\n"
            message += f"Type: {hard.type}\n"
            if hard.software_components:
                message += f"Software Components: {', '.join(name for name in soft_comp)}"
            else:
                message += f"Software Components: None\n"
        return message
