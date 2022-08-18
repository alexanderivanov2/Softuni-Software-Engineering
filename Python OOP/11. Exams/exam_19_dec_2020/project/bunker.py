from exam_19_dec_2020.project.supply.food_supply import FoodSupply
from exam_19_dec_2020.project.supply.water_supply import WaterSupply
from exam_19_dec_2020.project.medicine.painkiller import Painkiller
from exam_19_dec_2020.project.medicine.salve import Salve


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        foods = []
        for el in self.supplies:
            if isinstance(el, FoodSupply):
                foods.append(el)
        if not foods:
            raise IndexError("There are no food supplies left!")
        return foods

    @property
    def water(self):
        water = []
        for el in self.supplies:
            if isinstance(el, WaterSupply):
                water.append(el)
        if not water:
            raise IndexError("There are no water supplies left!")
        return water

    @property
    def painkillers(self):
        painkillers = []
        for el in self.medicine:
            if isinstance(el, Painkiller):
                painkillers.append(el)
        if not painkillers:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = []
        for el in self.medicine:
            if isinstance(el, Salve):
                salves.append(el)
        if not salves:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine):
        if survivor.needs_healing:
            last_medicine = self.painkillers[-1] if medicine == "Painkiller" else self.salves[-1]
            last_medicine.apply(survivor)
            self.medicine.remove(last_medicine)
            return f"{survivor.name} healed successfully with {medicine}"

    def sustain(self, survivor, sustenance):
        if survivor.needs_sustenance:
            last_supply = self.food[-1] if "Food" in sustenance else self.water[-1]
            last_supply.apply(survivor)
            self.supplies.remove(last_supply)
            return f"{survivor.name} sustained successfully with {sustenance}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
        for survivor in self.survivors:
            self.sustain(survivor, "Food")
            self.sustain(survivor, "Water")
