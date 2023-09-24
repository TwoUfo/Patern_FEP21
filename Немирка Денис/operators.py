from __future__ import annotations
from typing import TYPE_CHECKING
from bill import Bill

if TYPE_CHECKING:
    from customer import Customer


class Operator:
    def __init__(self, id: int, name: str, talkingCharge: float, messageCost: float, networkCharge: float, discountRate: int, total: int = 0) -> None:
        self.id = id
        self.name = name
        self._talkingCharge = talkingCharge
        self._messageCost = messageCost
        self._networkCharge = networkCharge
        self._discountRate = discountRate
        self.total = total

    # getters and setters
    @property
    def talkingCharge(self) -> float:
        return self._talkingCharge

    @talkingCharge.setter
    def talkingCharge(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError(
                f"Provided talking charge {value} is not of float type")
        self._talkingCharge = value

    @property
    def messageCost(self) -> float:
        return self._messageCost

    @messageCost.setter
    def messageCost(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError(
                f"Provided message cost {value} is not of float type")
        self._messageCost = value

    @property
    def networkCharge(self) -> float:
        return self._networkCharge

    @networkCharge.setter
    def networkCharge(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError(
                f"Provided network charge {value} is not of float type")
        self._networkCharge = value

    @property
    def discountRate(self) -> int:
        return self._discountRate

    @discountRate.setter
    def discountRate(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError(
                f"Provided discount rate {value} is not of integer type")
        self._discountRate = value

    # functions

    @staticmethod
    def createBill(customer_id: int) -> Bill:
        bill = Bill(customerID=customer_id)
        return bill

    def calculateTalkingCost(self, minute: int, customer: Customer) -> float:
        talkingCharge = self.talkingCharge
        if customer.age < 18 or customer.age > 65:
            talkingCharge -= self.discountRate
        self.total += minute*talkingCharge
        return minute*talkingCharge

    def calculateMessageCost(self, quantity: int, customer: Customer, customer2: Customer) -> float:
        messageCost = self.messageCost
        if customer.operators.id == customer2.operators.id:
            messageCost -= self.discountRate
        self.total += quantity*messageCost
        return quantity*messageCost

    def calculateNetworkCost(self, amount: float) -> float:
        self.total = amount*self.networkCharge
        return amount*self.networkCharge
