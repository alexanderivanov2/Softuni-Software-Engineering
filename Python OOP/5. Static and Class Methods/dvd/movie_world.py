class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        curr_customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if dvd in curr_customer.rented_dvds:
            return f"{curr_customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif curr_customer.age < dvd.age_restriction:
            return f"{curr_customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        curr_customer.rented_dvds.append(dvd)
        return f"{curr_customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        curr_customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if dvd not in curr_customer.rented_dvds:
            return f"{curr_customer.name} does not have that DVD"
        curr_customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{curr_customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = "\n".join(f"{self.customers[i]}" for i in range(len(self.customers)))
        result2 = "\n".join(f"{self.dvds[i]}" for i in range(len(self.dvds)))
        return result + "\n" + result2