from __future__ import annotations
from typing import TYPE_CHECKING
from bill import Bill

if TYPE_CHECKING:
    from customer import Customer  # Імпортуємо клас Customer для анотації типів

class Operator:
    """Клас, що зберігає інформацію про оператора мережі зв'язку."""

    def __init__(self, id: int, name: str, talking_charge: float,
                 message_cost: float, network_charge: float,
                 discount_rate: int) -> None:
        # Ініціалізуємо атрибути оператора
        self.id = id
        self.name = name
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        self.discount_rate = discount_rate

    @staticmethod
    def create_bill(limit: float, customer_id: int) -> Bill:
        # Статичний метод для створення рахунку клієнта
        bill = Bill(limit=limit, customer_id=customer_id)
        return bill

    def calc_talking_charge(self, duration: float, customer1: Customer, other_customer: Customer):
        # Метод для розрахунку вартості розмови
        talking_charge = self.talking_charge
        if customer1.age < 18 and other_customer.age < 18 or other_customer.age > 45 and other_customer.age > 45:
            talking_charge = talking_charge - self.discount_rate

        return talking_charge * duration

    def calc_message_cost(self, quantity: float, customer1: Customer, other_customer: Customer, name: str):
        # Метод для розрахунку вартості повідомлень
        message_cost = self.message_cost
        if customer1.operators[name].id and other_customer.operators[name].id:
            message_cost = message_cost - self.discount_rate
        if customer1.age < 18 and other_customer.age < 18 or other_customer.age > 45 and other_customer.age > 45:
            message_cost = message_cost - self.discount_rate

        return message_cost * quantity

    def calc_network_cost(self, amount: float):
        # Метод для розрахунку вартості підключення до мережі
        network_charge = self.network_charge
        if network_charge > amount:
            raise ValueError(f"You reached the limit. Operation is forbidden")
        else:
            return amount * network_charge

    # Задаємо геттери та сеттери для атрибутів оператора

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError(f"Provided name {value} is not of str type")
        self._name = value

    @property
    def talking_charge(self) -> float:
        return self._talking_charge

    @talking_charge.setter
    def talking_charge(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError(f"Provided talking charge {value} is not of float type")
        self._talking_charge = value

    @property
    def message_cost(self) -> float:
        return self._message_cost

    @message_cost.setter
    def message_cost(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError(f"Provided message cost {value} is not of float type")
        self._message_cost = value

    @property
    def network_charge(self) -> float:
        return self._network_charge

    @network_charge.setter
    def network_charge(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError(f"Provided network charge {value} is not of float type")
        self._network_charge = value

    @property
    def discount_rate(self) -> int:
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError(f"Provided discount rate {value} is not of int type")
        self._discount_rate = value
