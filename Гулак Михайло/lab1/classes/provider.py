from uuid import uuid4
from .customer import Customer


class Provider:
    def __init__(self, name, talking_charge=0, message_cost=0, network_charge=0):
        self.id = uuid4()
        self.name = name
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge

    def calculate_talking_cost(self, customer: Customer, duration: int) -> float:
        cost = self.talking_charge * duration

        if customer.discount_rate != 0:
            cost -= cost * customer.discount_rate

        return cost

    def calculate_message_cost(self, customer: Customer, quantity: int) -> float:
        cost = self.message_cost * quantity

        if customer.discount_rate != 0:
            cost -= cost * customer.discount_rate

        return cost

    def calculate_network_charge(self, customer: Customer, data_size: int) -> float:
        cost = self.network_charge * data_size

        if customer.discount_rate != 0:
            cost -= cost * customer.discount_rate

        return cost

    def __repr__(self):
        return f"Provider(id={self.id}, name={self.name}, talking_charge={self.talking_charge}, message_cost={self.message_cost}, network_charge={self.network_charge})"
