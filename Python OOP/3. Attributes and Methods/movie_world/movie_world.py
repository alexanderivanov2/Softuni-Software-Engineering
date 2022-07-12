class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        customers_info = ''
        dvds_info = ''
        for cust in self.customers:
            customers_info += f"{cust.id}: {cust.name} of age {cust.age} has {len(cust.rented_dvds)} rented DVD's" \
                             f" ({' '.join(dvd.name for dvd in cust.rented_dvds)})\n"
        for dvd in self.dvds:
            dvds_info += f"{dvd.id}: {dvd.name} ({dvd.creation_month} {dvd.creation_year}) has age restriction" \
                         f" {dvd.age_restriction}. Status: {'rented' if dvd.is_rented else 'not rented'}"
            if not dvd == self.dvds[-1]:
                dvds_info += '\n'
        return customers_info + dvds_info


    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def return_objects(customers, cus_id, dvds, dvd_id):
        find_customer = [cust for cust in customers if cus_id == cust.id]
        customer = find_customer[0] if len(find_customer) else None
        find_dvd = [dvd for dvd in dvds if dvd.id == dvd_id]
        dvd = find_dvd[0] if len(find_customer) else None
        return customer, dvd

    def add_customer(self, customer):
        if len(self.customers) == self.customer_capacity():
            return
        self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) == self.dvd_capacity():
            return
        self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer, dvd = self.return_objects(self.customers, customer_id, self.dvds, dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer, dvd = self.return_objects(self.customers, customer_id, self.dvds, dvd_id)
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"