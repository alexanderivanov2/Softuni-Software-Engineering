class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if len(Vet.animals) >= 5:
            return "Not enough space"
        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        if animal_name not in Vet.animals:
            return f"{animal_name} not in the clinic"
        if animal_name in self.animals:
            self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)
        return f"{animal_name} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {self.space - len(Vet.animals)} space left in clinic"


import unittest


class Tests(unittest.TestCase):


    def test_init(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        self.assertEqual(vet.name, "Bob")
        self.assertEqual(vet.animals, [])
        self.assertEqual(Vet.animals, [])
        self.assertEqual(Vet.space, 5)


    def test_register_successfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        vet2 = Vet("Peter")
        res = vet.register_animal("Doggy")
        self.assertEqual(res, "Doggy registered in the clinic")
        self.assertEqual(vet.animals, ["Doggy"])
        self.assertEqual(vet.animals, ["Doggy"])
        self.assertEqual(vet2.animals, [])


    def test_register_unsuccessfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        for i in range(6):
            vet.register_animal(str(i))
        res = vet.register_animal("Doggy")
        self.assertEqual(res, "Not enough space")
        self.assertEqual(len(Vet.animals), 5)
        self.assertEqual(len(vet.animals), 5)


    def test_unregister_successfull(self):
        vet = Vet("Bob")
        Vet.animals = []
        Vet.space = 5
        vet.register_animal("Kitty")
        res = vet.unregister_animal("Kitty")
        self.assertEqual(res, "Kitty unregistered successfully")
        self.assertEqual(vet.animals, [])
        self.assertEqual(Vet.animals, [])


if __name__ == "__main__":
    unittest.main()
