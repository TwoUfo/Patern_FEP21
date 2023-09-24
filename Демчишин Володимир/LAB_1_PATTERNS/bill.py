class Bill:
    #TODO: Holds bill implementation details.
    def __init__(self, limit: float, current_dept: float):
        self.limit = limit
        self.current_dept = current_dept

    def check(self, amount: float):
        if amount <= self.limit:
            return True
        else:
            return False

    def change(self, amount: float):
        self.limit += amount
        #return f"Limit has been risen to {self.limit}"

    def pay(self, amount: float) -> None:
        if self.current_dept:
            temp = self.current_dept - amount
            if temp < 0:
                self.current_debt = 0
            else:
                self.current_debt = temp
        #return f"Customer {self} paid {amount}"

    def add(self, amount: float):
        self.current_dept += amount
