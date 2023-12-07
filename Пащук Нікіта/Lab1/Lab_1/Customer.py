from Operator import Operator
from Bill import Bill


class Customer:
    def __init__(self, id: int, name: str, age: int, operator: Operator, bill: Bill):
        self.id = id
        self.name = name
        self.age = age
        self.Operator = operator
        self.Bill = bill

    def talk(self, minute: int, other_customer: 'Customer'):
        if self.Bill.check(self.Bill.current_debt):
            self.Bill.add(self.Operator.calculate_talking_cost(minute, self))
            return f"Customer {self.name} talked to customer {other_customer.name}"
        else:
            return "Limited amount was exceeded, operation was not done"

    def message(self, quantity: int, other_customer: 'Customer'):
        if self.Bill.check(self.Bill.current_debt):
            self.Bill.add(self.Operator.calculate_message_cost(quantity, self, other_customer))
            return f"Customer {self.name} sent message to customer {other_customer.name}"
        else:
            return "Limited amount was exceeded, operation was not done"

    def connection(self, amount: float):
        if self.Bill.check(self.Bill.current_debt):
            self.Bill.add(self.Operator.calculate_network_cost(amount))
            return f"Customer has connected to the internet while having {amount} MB"
        else:
            return "Limited amount was exceeded, operation was not done"

    def change_operator(self, Operators, wanted_id):
        current_id = self.Operator.id
        self.Operator = Operators[wanted_id]
        return f"Operator was changed from {current_id} to {wanted_id}"
