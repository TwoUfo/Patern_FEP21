from __future__ import annotations


class BillClass:
    def __init__(self, customer_id: int, current_debt: float = 0, limiting_amount: int = 200) -> None:
        self.limitingAmount = limiting_amount
        self.customerID = customer_id
        self.currentDebt = current_debt

    def __str__(self) -> str:
        return f"{self.currentDebt}"

    def check(self):
        if self.currentDebt > self.limitingAmount:
            return False
        else:
            return True

    def add(self, amount: float) -> None:
        temp = self.currentDebt + amount
        if temp < self.limitingAmount:
            self.currentDebt += temp
            print(f"Add {temp} to debt")
        else:
            raise ValueError(f"You reached the limit. Operation is forbidden")

    def pay(self, amount: float) -> None:
        temp = self.currentDebt - amount
        if temp < 0:
            self.currentDebt = 0
        else:
            self.currentDebt = temp
        print(f"Customer {self.customerID} paid ${temp}")

    def change_the_limit(self, amount: float) -> None:
        self.limitingAmount += amount
        print(f"Limit has been risen to {self.limitingAmount}")
