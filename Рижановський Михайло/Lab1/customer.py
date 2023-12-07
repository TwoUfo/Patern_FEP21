from __future__ import annotations
from typing import Dict

from operators import Operator
from bill import Bill


class Customer:


    def __init__(self, operators: Dict[Operator], bills: Dict[Bill], id: int, first_name: str, second_name: str, age: int) -> None:
        # Ініціалізуємо атрибути клієнта
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.operators = operators
        self.bills = bills

    def _generate_bills(self) -> dict:
        # Генерує рахунки для клієнта для кожного оператора
        bills = {}
        for operator_id, operator in self.operators.items():
            #strange activity
            bills[operator_id] = operator.create_bill(limit=32, customer_id=self.id)
        return bills

    # Задаємо геттери та сеттери для атрибутів клієнта
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError(f"Provided name {value} is not of int type")
        self._id = value

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError(f"Provided name {value} is not of string type")
        self._first_name = value

    @property
    def second_name(self) -> str:
        return self._second_name

    @second_name.setter
    def second_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError(f"Provided second name {value} is not of string type")
        self._second_name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError(f"Provided age {value} is not of int type")
        self._age = value

    def talk(self, minutes: float, operator_name: Customer, operator_name2: Customer, name: str) -> None:
        # Метод для проведення розмови
        operator = self.operators[name]
        cost = operator.calc_talking_charge(duration=minutes, customer1=operator_name, other_customer=operator_name2)
        bill = self.bills[name]
        bill.add(debt=cost)
        print(f"Customer {self.first_name} {self.second_name} talked to {operator_name2.first_name} {operator_name2.second_name} for {minutes} minutes and costs {cost}")

    def message(self, quantity: float, operator_name: Customer, other_customer1: Customer, name: str) -> None:
        # Метод для відправлення повідомлень
        operator = self.operators[name]
        cost = operator.calc_message_cost(quantity=quantity, customer1=operator_name, other_customer=other_customer1, name=name)
        bill = self.bills[name]
        bill.add(debt=cost)
        print(f"Customer {self.first_name} chats to {other_customer1.first_name} with cost {cost}")

    def connect(self, traffic: float, operator_name: str) -> None:
        # Метод для підключення до мережі
        operator = self.operators[operator_name]
        cost = operator.calc_network_cost(amount=traffic)
        bill = self.bills[operator_name]
        bill.add(debt=cost)
        print(f"Customer {self.first_name} {self.second_name} connected to the network with {traffic} traffic")

    def change_limit(self, value: float, operator_name: str) -> None:
        # Метод для зміни ліміту рахунку
        bill = self.bills[operator_name]
        bill.change_limit(value)
        print(f"Changed the limit to {value} for Operator {operator_name}")

    def view_bills(self) -> None:
        # Метод для перегляду рахунків клієнта
        for operator_name, bill in self.bills.items():
            print(f"Operator: {operator_name}, Bill: {bill}")

    def pay_bill(self, operator_name: str, amount: float) -> None:
        # Метод для оплати рахунку
        if operator_name in self.bills:
            bill = self.bills[operator_name]
            amount = bill.current_debt
            if bill.check_limit(amount):
                bill.pay(amount)
                print(f"Customer {self.first_name} paid {amount} for Operator {operator_name}'s bill.")
            else:
                print(f"The payment amount {amount} exceeds the bill limit for Operator {operator_name}.")
        else:
            print(f"Operator {operator_name} not found in customer's operators.")

    def pay_off_debt(self, operator_name: str) -> None:
        # Метод для погашення всього боргу за рахунком
        if operator_name in self.bills:
            bill = self.bills[operator_name]
            bill.pay(bill.current_debt)
            print(f"Customer {self.first_name} paid off the entire debt for Operator {operator_name}.")
        else:
            print(f"Operator {operator_name} not found in customer's operators.")
