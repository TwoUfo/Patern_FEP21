import json
from customer import Customer
from operatorClass import Operator
from bill import Bill

'''Open and parse JSON file with customer info'''
with open('baseCustomer.json') as file:
    data = json.load(file)

Customers = []
for item in data['items']:
    Customers.append(Customer(
        item['id'],
        item['name'],
        item['surname'],
        item['age'],
        Bill(item['bill']['limit'], item['bill']['currDebt']),
        item['operator_id']
    ))
file.close()


'''Open and parse JSON file with operator info'''


with open('baseOperator.json') as file:
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

for item in Customers:
    print("-----------------")
    print(item.id)
    print(item.age)
    print(item.bill.limit)
    print(item.bill.currDebt)
    print(item.name)
    print(item.surname)
    print("-----------------")

for item in Operators:
    print("-----------------")
    print(item.id)
    print(item.networkCharge)
    print("-----------------")

print(Customers[0].talk(60, Customers[1]))

print(Customers[0].message(15, Customers[1]))

print(Customers[0].connect(60.0))






