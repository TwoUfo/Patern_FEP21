class Customer:
    def __init__(self, id, name, surname, age, bill, operator):
        self.id = id
        self.name = name
        self.surname = surname
        self._age = age
        self.bill = bill
        self._operator = operator

    def talk(self, minute, otherCustomer):
        self.bill._currDebt += self.operator.calculateTalkingCost(minute, currCustomer=self)
        return f"Customer {self.name} {self.surname} talked with customer {otherCustomer.name} {otherCustomer.surname} {minute} minutes."

    def message(self, quantity, otherCustomer):
        self.bill._currDebt += self.operator.calculateMessageCost(quantity, currCustomer=self, otherCustomer=otherCustomer)
        return f"Customer {self.name} {self.surname} sent {quantity} messages to {otherCustomer.name} {otherCustomer.surname}. "

    def connect(self, amount):
        if self.bill.check(amount):
            self.bill._currDebt += self.operator.calculateNetworkCost(amount)
            return f"Customer {self.name} {self.surname} connected to network ({amount} mbps)."
        else:
            return "Limit error"

    def changeOperator(self, id, operators):
        self.operator = operators[id]

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, newValue):
        self._age = newValue

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, newValue):
        self._operator = newValue
