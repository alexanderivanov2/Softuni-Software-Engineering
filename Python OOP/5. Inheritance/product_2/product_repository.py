class ProductRepository:
    def __init__(self):
        self.products = []

    def __repr__(self):
        return '\n'.join(f'{product.name}: {product.quantity}' for product in self.products)


    def finding_object_with_name(self, products, product_name):
        for product in products:
            if product.name == product_name:
                return product

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        find_object = self.finding_object_with_name(self.products, product_name)
        return find_object

    def remove(self, product_name):
        find_remove_object = self.finding_object_with_name(self.products, product_name)
        if find_remove_object:
            self.products.remove(find_remove_object)
