from __future__ import annotations
from bill import Bill
from operators import Operator
from customer import Customer


def main():
    operator1 = Operator(0, 'Marvin', 0.2, 0.9, 0.8, 0.1)
    operator2 = Operator(1, 'Smith', 0.8, 1.4, 0.2, 0.5)

    bill1 = Bill(200, 0)
    bill2 = Bill(564, 1)

    customer1 = Customer(0, 'Walter', 19, operator1, bill1, 200)
    customer2 = Customer(1, 'Butcher', 28, operator2, bill2, 564)

    customer1.talk(1, customer1)
    customer1.message(14, customer1, customer2)
    customer1.connection(40.32)

    customer2.talk(1, customer2)
    customer1.message(14, customer2, customer1)
    customer1.connection(54.3)

    print(f"Customer 1 {customer1.name}'s bill amount is {customer1._bills}")
    print(f"Customer 2 {customer2.name}'s bill amount is {customer2._bills}")


if __name__ == "__main__":
    main()
