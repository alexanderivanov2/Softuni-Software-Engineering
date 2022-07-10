class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
        self.taken_size = 0

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @classmethod
    def small_shop(cls, name: str, type: str):
        size = 10
        return cls(name, type, size)

    def add_item(self, item_name: str):
        if self.capacity == self.taken_size:
            return "Not enough capacity in the shop"

        if item_name in self.items:
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1
        self.taken_size += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name:str, amount:int):
        if item_name not in self.items or amount > self.items.get(item_name):
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        self.taken_size -= amount
        return f"{amount} {item_name} removed from the shop"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))

# import unittest
#
# class ShopTests(unittest.TestCase):
#     def setUp(self):
#         self.fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
#
#     def test_add_item_success(self):
#         result = self.fresh_shop.add_item("Bananas")
#         self.assertEqual(self.fresh_shop.items["Bananas"], 1)
#         self.assertEqual(result, "Bananas added to the shop")
#
#     def test_remove_item_success(self):
#         self.fresh_shop.add_item("Bananas")
#         result = self.fresh_shop.remove_item("Bananas", 1)
#         self.assertEqual(result, "1 Bananas removed from the shop")
#
#     def test_remove_item_unsuccessful(self):
#         self.fresh_shop.add_item("Bananas")
#         result = self.fresh_shop.remove_item("Tomatoes", 2)
#         self.assertEqual(result, "Cannot remove 2 Tomatoes")
#
#     def test_repr(self):
#         self.assertEqual(repr(self.fresh_shop), "Fresh Shop of type Fruit and Veg with capacity 50")
#
#
# if __name__ == "__main__":
#     unittest.main()
