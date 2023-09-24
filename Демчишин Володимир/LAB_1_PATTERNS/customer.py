class Customer:
    def __init__(self, id: int, name: str, age: int, bill, operator) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.bill = bill
        self.operator = operator

    def talk(self, minute: float, second_customer) -> str:
        # TODO: using operator, calculate talk rate
        if self.bill.check(self.bill.current_dept):
            self.bill.add(self.operator.calculateTalkingCost(minute, self))
            return (f"{self.name} talked with {second_customer.name} {minute} minutes. "
                    f"{self.name} have current dept {self.bill.current_dept}$")
        else:
            return f"{self.name} reached the limit. Operation error"

    def message(self, quantity: float, second_customer) -> str:
        # TODO: using operator, calculate message cost
        if self.bill.check(self.bill.current_dept):
            self.bill.add(self.operator.calculateMessageCost(quantity, self, second_customer))
            return (f"{self.name} sent {quantity} messages to {second_customer.name}. "
                    f"{self.name} have current dept {self.bill.current_dept}$")
        else:
            return f"{self.name} reached the limit. Operation error"

    def connect(self, amount: float) -> str:
        # TODO: using operator, calculate network cost
        if self.bill.check(self.bill.current_dept):
            self.bill.add(self.operator.calculateNetworkCost(amount))
            return (f"{self.name} connected to network ({amount} mbps). "
                    f"{self.name} have current dept {self.bill.current_dept}$")
        else:
            return f"{self.name} reached the limit. Operation error"

    def change(self, amount: float) -> str:
        # TODO: using operator, change limit
        if self.bill.change(self.bill.limit):
            self.bill.change(amount)
        return f"{self.name} limit rised to {self.bill.limit}$"

    def pay_debt(self, amount: float) -> str:
        # TODO: using operator, change current_dept
        if self.bill.pay(self.bill.current_dept):
            self.bill.pay(amount)
        return f"{self.name} pay {amount}$" #, and now have dept {self.bill.current_dept}$"

    def add_debt(self, amount: float) -> str:
        # TODO: using operator, change current_dept
        if self.bill.add(self.bill.current_dept):
            self.bill.add(amount)
        return f"{self.name} dept raised {amount}$, and now have dept {self.bill.current_dept}$"