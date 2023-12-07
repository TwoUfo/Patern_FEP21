class Bill:
    def __init__(self, limiting_amount: float, current_debt=0):
        self.limitingAmount = limiting_amount
        self.current_debt = current_debt

    def check(self, current_debt: float):
        if self.current_debt > self.limitingAmount:
            return False
        else:
            return True

    def add(self, amount: float):
        if self.current_debt + amount >= self.limitingAmount:
            return "Cannot add: limit exceeded"
        else:
            self.current_debt += amount
        return f"Customer has added {amount} to his debt, current debt is {self.current_debt}"

    def pay(self, amount: float):
        if self.current_debt - amount <= 0:
            return "Cannot pay: negative value"
        else:
            self.current_debt -= amount
        return f'Customer has payed {amount} for his debt, current debt is {self.current_debt}'

    def check_limit(self):
        return f"Your current limit is {self.limitingAmount}"

    def change_the_limit(self, amount: float):
        self.limitingAmount = amount
        return f'Your new limit is {self.limitingAmount}'
