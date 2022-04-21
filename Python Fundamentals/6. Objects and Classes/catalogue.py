class Catalogue:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [el for el in self.products if el[0] == first_letter]

    def __repr__(self):
        self.products = sorted(self.products)
        return f"Items in the {self.name} catalogue:\n" + '\n'.join(self.products)


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)