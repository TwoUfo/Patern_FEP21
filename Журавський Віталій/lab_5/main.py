from CreditCard import CreditCard
from BankCustomer import *
from BankInfo import *
from fastapi import FastAPI
import json

# card1 = CreditCard('Vitalii', 1618664, 5000, 2024, '874')
# bank = BankInfo('OBank', 'UA_O_BANK')
# customer1 = BankCustomer(PersonalInfo('Vitalii', 18, 'student'), card1, bank)
# corp_customer = CorporateBankCustomer(customer1)
#
# print(corp_customer.give_details())

app = FastAPI()

customers = []
credit_cards = []
banks = []


@app.get('/')
def create_objects():
    with open('BankInfoData.json') as file:
        bank_data = json.load(file)
    with open('CreditCardData.json') as file:
        card_data = json.load(file)
    with open('BankCustomerData.json') as file:
        customer_data = json.load(file)

    for iter, item in enumerate(bank_data):
        banks.append(BankInfo(
            item['bank_name'],
            item['holder_name']
        ))

        for inner_item in card_data:
            credit_cards.append(CreditCard(
                inner_item['client'],
                inner_item['account_number'],
                inner_item['credit_limit'],
                inner_item['grace_period'],
                inner_item['cvv']
            ))

        for iter1, inner_item_1 in enumerate(customer_data):
            customers.append(BankCustomer(
                PersonalInfo(
                    inner_item_1['name'],
                    inner_item_1['age'],
                    inner_item_1['curr_position']
                ),
                credit_cards[iter1],
                banks[iter]
            ))

        return customers[0].give_details()


@app.post('/transaction/')
def transaction(user_id: int, transaction_info: str):
    customers[user_id].bank_info.add_transaction(
        customers[user_id].credit_card.account_number,
        transaction_info
    )

    return customers[user_id].give_details()

