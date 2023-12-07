class Customer:
    def __init__(self, id, name, surname, age, bill, operator):
        self.id = id
        self.name = name
        self.surname = surname
        self._age = age
        self.bill = bill
        self._operator = operator

    def __str__(self):
        return f'{self.name} {self.surname} | current bill: debt={self.bill.currDebt}, limit={self.bill.limit} | current operator: {self.operator.id}\n'

    def talk(self, minute, otherCustomer):
        if self.bill.check(self.bill.currDebt):
            self.bill.add(self.operator.calculateTalkingCost(minute, currCustomer=self))
            return f"Customer {self.name} {self.surname} talked with customer {otherCustomer.name} {otherCustomer.surname} {minute} minutes."
        else:
            return "Limit error"

    def message(self, quantity, otherCustomer):
        if self.bill.check(self.bill.currDebt):
            self.bill.add(self.operator.calculateMessageCost(quantity, currCustomer=self, otherCustomer=otherCustomer))
            return f"Customer {self.name} {self.surname} sent {quantity} messages to {otherCustomer.name} {otherCustomer.surname}. "
        else:
            return "Limit error"

    def connect(self, amount):
        if self.bill.check(self.bill.currDebt):
            self.bill.add(self.operator.calculateNetworkCost(amount))
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
