import json
from customer import Customer
from Operators import Operator
from bill import Bill

with open('stub_customer.json') as file:
    data = json.load(file)

Customers = []
for item in data['items']:
    Customers.append(Customer(
        item['id'],
        item['name'],
        item['age'],
        Bill(item['bill']['limit'], item['bill']['current_debt']),
        item['operator_id']
    ))
file.close()


with open('stub_operator.json') as file:
    data = json.load(file)

Operators = []
for item in data['items']:
    Operators.append(Operator(
        item['id'],
        item['talkingCharge'],
        item['messageCharge'],
        item['networkCharge'],
        item['discountRate'],
        item['discountMessageRate']
    ))
file.close()

for item in Customers:
    item.operator = Operators[item.operator]


print(Customers[1].talk(25, Customers[2]))

print(Customers[2].message(10000, Customers[3]))

print(Customers[2].connect(10))

print(Customers[1].change(1))

print(Customers[1].add_debt(6))

print(Customers[1].pay_debt(4))


