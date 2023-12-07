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

'''Add operators to customers fields'''
for item in Customers:
    item.operator = Operators[item.operator]
