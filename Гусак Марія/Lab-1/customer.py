class Customer:
    def __init__(self, id_customer, name, age, operator, balance,  bill_limit):
        self.id_customer = id_customer
        self.name = name
        self.age = age
        self.operator = operator
        self.balance = balance
        self.bill_limit = bill_limit

    def talk(self, minute):
        if self.balance >= minute and self.age >= 18 and self.bill_limit is None or self.balance < self.bill_limit:
            self.balance -= minute
        else:
            print(f"You do not have enough balance to talk.")

    def message(self, messages):
        if self.balance >= messages and self.age >= 18 and self.bill_limit is None or self.balance < self.bill_limit:
            self.balance -= messages
        else:
            print(f"You do not have enough balance to send messages.")

    def connection(self, internet_cost):
        if self.balance >= internet_cost and self.age >= 18 and self.bill_limit is None or self.balance < self.bill_limit:
            self.balance -= internet_cost
        else:
            print(f"You can not connect to the internet ")

