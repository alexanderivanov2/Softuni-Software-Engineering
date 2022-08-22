from exam_5.hardware.heavy_hardware import HeavyHardware
from exam_5.hardware.power_hardware import PowerHardware
from exam_5.software.express_software import ExpressSoftware
from exam_5.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hard = [h for h in System._hardware if h.name == hardware_name]
        if not hard:
            return "Hardware does not exist"
        soft = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hard[0].install(soft)
        System._software.append(soft)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hard = [h for h in System._hardware if h.name == hardware_name]
        if not hard:
            return "Hardware does not exist"
        soft = LightSoftware(name, capacity_consumption, memory_consumption)
        hard[0].install(soft)
        System._software.append(soft)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hard = [h for h in System._hardware if h.name == hardware_name]
        soft = [s for s in System._software if s.name == software_name]
        if soft and hard:
            hard[0].uninstall(soft[0])
            System._software.remove(soft[0])
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        message = f"System Analysis\nHardware Components: {len(System._hardware)}\nSoftware Components: {len(System._software)}\n"
        total_memory = sum([s.memory_consumption for s in System._software])
        total_memory_hard = sum([h.memory for h in System._hardware])
        message += f"Total Operational Memory: {total_memory} / {total_memory_hard}\n"
        total_capacity = sum([s.capacity_consumption for s in System._software])
        total_capacity_hard = sum([h.capacity for h in System._hardware])
        message += f"Total Capacity Taken: {total_capacity} / {total_capacity_hard}"
        return message

    @staticmethod
    def system_split():
        message = []
        for h in System._hardware:
            exp_soft = [s for s in h.software_components if s.software_type == "Express"]
            light_soft = [s for s in h.software_components if s.software_type == "Light"]
            new_message = f"Hardware Component - {h.name}\n"
            new_message += f"Express Software Components: {len(exp_soft)}\nLight Software Components: {len(light_soft)}\n"
            new_message += f"Memory Usage: {h.current_memory} / {h.memory}\nCapacity Usage: {h.current_capacity} / {h.capacity}\n"
            soft_comp = [s.name for s in h.software_components]
            if soft_comp:
                new_message += f"Type: {h.hardware_type}\nSoftware Components: {', '.join(soft_comp)}"
            else:
                new_message += f"Type: {h.hardware_type}\nSoftware Components: None"
            message.append(new_message)
        return "\n".join(message)

System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())
