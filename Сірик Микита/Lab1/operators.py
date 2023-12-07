from __future__ import annotations
from typing import TYPE_CHECKING

from Bill import BillClass

if TYPE_CHECKING:
    from Customer import CustomerClass


class OperatorClass:
    def __init__(self, operator_id: int, name: str, talking_charge: float, message_cost: float,
                 network_charge: float, discount_rate: int, total: int = 0) -> None:
        self.id = operator_id
        self.name = name
        self._talkingCharge = talking_charge
        self._messageCost = message_cost
        self._networkCharge = network_charge
        self._discountRate = discount_rate
        self.total = total

    @property
    def talking_charge(self) -> float:
        return self._talkingCharge

    @talking_charge.setter
    def talking_charge(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError(f"Provided talking charge {value} is not of float type")
        self._talkingCharge = value

    @property
    def messageCost(self) -> float:
        return self._messageCost

    @messageCost.setter
    def messageCost(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError(f"Provided message cost {value} is not of float type")
        self._messageCost = value

    @property
    def networkCharge(self) -> float:
        return self._networkCharge

    @networkCharge.setter
    def networkCharge(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError(f"Provided network charge {value} is not of float type")
        self._networkCharge = value

    @property
    def discountRate(self) -> int:
        return self._discountRate

    @discountRate.setter
    def discountRate(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError(f"Provided discount rate {value} is not of integer type")
        self._discountRate = value

    # functions

    @staticmethod
    def createBill(customer_id: int) -> BillClass:
        bill = BillClass(customer_id=customer_id)
        return bill

    def calculate_talking_cost(self, minute: int, customer: CustomerClass) -> float:
        talkingCharge = self.talking_charge
        if customer.age < 18 or customer.age > 65:
            talkingCharge -= self.discountRate
        self.total += minute * talkingCharge
        return minute * talkingCharge

    def calculate_message_cost(self, quantity: int, customer: CustomerClass, customer2: CustomerClass) -> float:
        messageCost = self.messageCost
        if customer.operators.id == customer2.operators.id:
            messageCost -= self.discountRate
        self.total += quantity * messageCost
        return quantity * messageCost

    def calculate_network_cost(self, amount: float) -> float:
        self.total = amount * self.networkCharge
        return amount * self.networkCharge
