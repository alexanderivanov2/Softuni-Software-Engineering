class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def get_searched_object(place, id):
        searched_object = [x for x in place if x.id == id][0]
        return searched_object

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.get_searched_object(self.subscriptions, subscription_id)
        customer = self.get_searched_object(self.customers, subscription.customer_id)
        trainer = self.get_searched_object(self.trainers, subscription.trainer_id)
        plan = self.get_searched_object(self.plans, subscription.trainer_id)
        equipment = self.get_searched_object(self.equipment, plan.equipment_id)
        return f"Subscription <{subscription.id}> on {subscription.date}\n" \
               f"Customer <{customer.id}> {customer.name}; Address: {customer.address}; Email: {customer.email}\n" \
               f"Trainer <{trainer.id}> {trainer.name}\nEquipment <{equipment.id}> {equipment.name}\n" \
               f"Plan <{plan.id}> with duration {plan.duration} minutes"

