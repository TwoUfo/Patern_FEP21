from fastapi import FastAPI
from DB import TableCard, TableBankInfo, TableBankCustomer, TableCreditHistory, engine, session
from CreditCard import create_credit_card
from BankInfo import BankInfo
from BankCustomer import BankCustomer, PersonalInfo
from Models import *

app = FastAPI()

connection = engine.connect()


@app.post("/PostData")
def post_data(card: CreditCardModel, bank_info: BankInfoModel, bank_customer: BankCustomerModel):
    """Post data for credit card, bank and it's customer"""
    credit_card_data = TableCard(card.account_number, card.client, card.credit_limit, card.grace_period, card.cvv)
    session.add(credit_card_data)
    session.commit()

    bank_info_data = TableBankInfo(bank_info.bank_name, card.client, card.account_number)
    session.add(bank_info_data)
    session.commit()

    bank_customer_data = TableBankCustomer(bank_info_data.id, bank_customer.contact_info, bank_customer.birth_date,
                                           bank_customer.employment, bank_customer.income_per_year)
    session.add(bank_customer_data)
    session.commit()
    return_dict = {
        "credit card": credit_card_data,
        "bank info": bank_info_data,
        "bank customer": bank_customer_data
    }
    return return_dict


@app.get('/Customer-bank_data')
def get_data(account_number: str):
    """Get data related to account number (card data, bank data etc.)"""
    card_data = session.query(TableCard).filter(TableCard.account_number == account_number).first()
    if card_data:
        bank_info_data = session.query(TableBankInfo).filter(TableBankInfo.account_number == account_number).first()
        bank_customer_data = (session.query(TableBankCustomer).filter
                              (TableBankCustomer.bank_id == bank_info_data.id).first())
        credit_history_data = session.query(TableCreditHistory).filter(
            TableCreditHistory.sender_account_number == account_number).all()
        if not credit_history_data:
            credit_history_data = {}
        credit_history = {
            account_number: (obj.recipient_account_number, obj.amount) for obj in credit_history_data
        }

        customer_bank_info = BankCustomer(personal_info=PersonalInfo(
            create_credit_card(card_data.client, account_number, card_data.credit_limit, card_data.grace_period,
                               card_data.cvv), bank_customer_data.contact_info, bank_customer_data.birth_date,
            bank_customer_data.employment, bank_customer_data.income_per_year),
            bank_details=BankInfo(bank_info_data.bank_name, card_data.client,
                                  bank_info_data.account_number, credit_history))
        return customer_bank_info.give_details()
    else:
        return 'There is no such account'


@app.post('/Transaction')
def transaction(transaction_details: CreditHistoryModel):
    """Make a transaction between two accounts"""
    bank = session.query(TableBankInfo).filter(TableBankInfo.account_number == transaction_details.sender).first()
    new_transaction = TableCreditHistory(bank.bank_name, transaction_details.sender, transaction_details.recipient,
                                         transaction_details.amount)
    session.add(new_transaction)
    session.commit()
    return 'Transaction was carried successfully'
