from __future__ import annotations

from typing import Dict

from Bill import BillClass
from Operators import OperatorClass


class CustomerClass:
    """Holds customer's class"""

    def __init__(self, customer_id: int, name: str = "test", age: int = 0, operators: Dict[OperatorClass] = None,
                 bills: Dict[BillClass] = None, limiting_amount: float = 0, total: float = 0) -> None:
        self.id = customer_id
        self.name = name
        self._age = age
        self._operators = operators
        self._bills = self._generate_bill()
        self.limitingAmount = limiting_amount

    def __str__(self):
        return f"{self.name}"

    # getters and setters
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError(f"Provided age {value} is not of integer type")
        self._age = value

    @property
    def operators(self) -> dict:
        return self._operators

    @operators.setter
    def operators(self, value: dict) -> None:
        if not isinstance(value, dict):
            raise ValueError(f"Provided operators {value} is not of dictionary type")
        self._operators = value

    @property
    def bill(self) -> dict:
        return self._bills

    @bill.setter
    def bill(self, value: dict) -> None:
        if not isinstance(value, dict):
            raise ValueError(f"Provided bill {value} is not of dictionary type")
        self._bill = value

    def _generate_bill(self) -> BillClass:
        return OperatorClass.createBill(customer_id=self.id)

    def talk(self, minute: int, customer: CustomerClass) -> str:
        if self._bills.check():
            self._bills.add(self._operators.calculate_talking_cost(minute=minute, customer=customer))
            return f"Customer{self.name} talked to customer{customer.name}"
        else:
            return "Limited amount was exceeded, operation was not done"

    def message(self, quantity: int, customer: CustomerClass, otherCustomer: CustomerClass) -> str:
        if self._bills.check():
            self._bills.add(OperatorClass.calculate_message_cost(self._operators, quantity, customer, otherCustomer))
            return f"Customer{self.name} sent message to customer{otherCustomer.name}"
        else:
            return "Limited amount was exceeded, operation was not done"

    def connection(self, amount: float) -> str:
        if self._bills.check():
            self._bills.add(OperatorClass.calculate_network_cost(self.operators, amount=amount))
            return f"Customer has connected to the internet while having {amount} MB"
        else:
            return "Limited amount was exceeded, operation was not done"


