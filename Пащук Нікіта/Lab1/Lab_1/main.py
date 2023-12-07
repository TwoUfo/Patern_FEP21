import json
from Customer import Customer
from Operator import Operator
from Bill import Bill

Bills = []
Customers = []
Operators = []

with open('Operators.json') as operators_data:
    operators = json.load(operators_data)
for opera in operators["operator_data"]:
    Operators.append(Operator(
        opera["id"],
        opera["talkingCharge"],
        opera["messageCost"],
        opera["networkCharge"],
        opera["discountRate"]))

with open('Customers.json') as persons_data:
    received_data = json.load(persons_data)

for cust in received_data["persons_data"]:
    Customers.append(Customer(
        cust["id"],
        cust["name"],
        cust["age"],
        Operators[cust["operator"]],
        Bill(cust["bill"])))
"""Testing results"""

"""Customer's methods with checking balance"""

"""talk"""
print(Customers[0].Bill.current_debt, Customers[0].Bill.limitingAmount)
print(Customers[0].talk(10, Customers[1]))
print(Customers[0].Bill.current_debt, Customers[0].Bill.limitingAmount)
print('\t')
"""message"""
print(Customers[0].Bill.current_debt, Customers[0].Bill.limitingAmount)
print(Customers[0].message(5, Customers[2]))  # change customer to check if check() method works correctly
print(Customers[0].Bill.current_debt, Customers[0].Bill.limitingAmount)
print('\t')
"""connection"""
print(Customers[0].Bill.current_debt, Customers[0].Bill.limitingAmount)
print(Customers[0].connection(200))
print(Customers[0].Bill.current_debt, Customers[0].Bill.limitingAmount)
print('\t')
"""changing operator"""
print(Customers[0].Operator.id)
print(Customers[0].change_operator(Operators, 3))
print(Customers[1].Operator.id)
print('\t')

"""Operations with customer's bill"""

"""Add method"""
print(Customers[0].Bill.current_debt, Customers[0].Bill.limitingAmount)
print(Customers[0].Bill.add(10))
print(Customers[0].Bill.current_debt, Customers[0].Bill.limitingAmount)
print('\t')
"""Pay method"""
print(Customers[0].Bill.current_debt, Customers[0].Bill.limitingAmount)
print(Customers[0].Bill.pay(10))
print(Customers[0].Bill.current_debt, Customers[0].Bill.limitingAmount)
print('\t')
"""Check limit and change limit methods"""
print(Customers[0].Bill.check_limit())
print(Customers[0].Bill.change_the_limit(500))
print(Customers[0].Bill.check_limit())
