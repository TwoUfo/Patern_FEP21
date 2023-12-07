import unittest
from unittest import mock
from customer import Customer
from bill import Bill
from operatorClass import Operator
from main import Customers, Operators


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer(0, 'a', 'b', 20, Bill(100, 20), Operator(0, 0.2, 0.5, 1, 0.05, 0.1))
        self.customer2 = Customer(1, 'c', 'd', 35, Bill(100, 0), Operator(0, 0.19, 0.4, 1, 0.06, 0.2))

    def test_talk(self):
        message = self.customer1.talk(10, self.customer2)
        self.assertEqual(message, f"Customer {self.customer1.name} {self.customer1.surname} talked with customer {self.customer2.name} {self.customer2.surname} 10 minutes.")

        print(Customers[0].talk(12, Customers[2]))
        print(Customers[0])
        print(Customers[1].talk(20, Customers[5]))
        print(Customers[1])

    def test_message(self):
        message = self.customer1.message(3, self.customer2)
        self.assertEqual(message, f"Customer {self.customer1.name} {self.customer1.surname} sent {3} messages to {self.customer2.name} {self.customer2.surname}. ")

        print(Customers[3].message(3, Customers[4]))
        print(Customers[3])
        print(Customers[0].message(4, Customers[0]))
        print(Customers[0])

    def test_connect(self):
        message = self.customer1.connect(80)
        self.assertEqual(message, f"Customer {self.customer1.name} {self.customer1.surname} connected to network ({80} mbps).")

        print(Customers[2].connect(80))
        print(Customers[2])

    def test_pay(self):
        self.customer1.bill.pay(15)
        self.assertEqual(self.customer1.bill.currDebt, 5)

        print(f'current {Customers[2].name} {Customers[2].surname} debt: {Customers[2].bill.currDebt}')
        Customers[2].bill.pay(50)
        print(f'new {Customers[2].name} {Customers[2].surname} debt: {Customers[2].bill.currDebt}')
        print(Customers[2])

    def test_change_operator(self):
        self.customer1.changeOperator(5, Operators)
        self.assertEqual(self.customer1.operator.id, 5)

        print(f'old {Customers[3].name} {Customers[3].surname} operator: {Customers[3].operator.id}')
        Customers[3].changeOperator(2, Operators)
        print(f'new {Customers[3].name} {Customers[3].surname} operator: {Customers[3].operator.id}')
        print(Customers[3])

    def test_change_limit(self):
        self.customer1.bill.changeLimit(150)
        self.assertEqual(self.customer1.bill.limit, 150)

        print(f'old {Customers[5].name} {Customers[5].surname} limit: {Customers[5].bill.limit}')
        Customers[5].bill.changeLimit(200)
        print(f'new {Customers[5].name} {Customers[5].surname} limit: {Customers[5].bill.limit}')
        print(Customers[5])


if __name__ == '__main__':
    unittest.main()
