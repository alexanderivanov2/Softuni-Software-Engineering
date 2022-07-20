class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        result = [p for p in self.products if p.name == product_name]
        return result[0] if result else result

    def remove(self, product_name):
        if self.find(product_name):
            self.products.remove(self.find(product_name))

    def __repr__(self):
        result = "\n".join(f"{p.name}: {p.quantity}" for p in self.products)
        return result


