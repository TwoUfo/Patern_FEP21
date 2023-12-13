from bill import Bill


class Operator:
    def __init__(self, id_operator, name_operator, talking_charge_per_minute, message_cost_per_message, network_charge,
                 discount_rate):
        self.id_operator = id_operator
        self.name_operator = name_operator
        self.talking_charge_per_minute = talking_charge_per_minute
        self.message_cost_per_message = message_cost_per_message
        self.network_charge = network_charge
        self.discountRate = discount_rate
        self.bill = None

    def calculate_talking_cost(self, minutes):
        talking_charge = minutes * self.talking_charge_per_minute
        return talking_charge

    def calculate_message_cost(self, messages):
        message_cost = messages * self.message_cost_per_message
        return message_cost

    def calculate_internet_cost(self, internet_cost):
        return internet_cost * self.network_charge

    def generate_bill(self, minutes, messages, internet_cost):
        total_cost = self.calculate_talking_cost(minutes) + self.calculate_message_cost(messages) + self.calculate_internet_cost(internet_cost)
        self.bill = Bill(self.id_operator, total_cost)
