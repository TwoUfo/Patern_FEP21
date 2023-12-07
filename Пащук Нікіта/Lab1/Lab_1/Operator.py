class Operator:
    def __init__(self, id: int, talking_charge: float, message_cost: float, network_charge: float, discount_rate: int):
        self.id = id
        self.talkingCharge = talking_charge
        self.messageCost = message_cost
        self.networkCharge = network_charge
        self.discountRate = discount_rate

    def calculate_talking_cost(self, minute: int, customer):
        talking_cost = minute * self.talkingCharge
        if 65 > customer.age < 18:
            talking_cost -= talking_cost * self.discountRate
        return talking_cost

    def calculate_message_cost(self, quantity: int, customer, other_customer):
        total_message_cost = quantity * self.messageCost
        if customer.Operator == other_customer.Operator:
            total_message_cost -= total_message_cost * self.discountRate
        return total_message_cost

    def calculate_network_cost(self, amount: float):
        return amount * self.networkCharge
