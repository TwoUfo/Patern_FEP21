import json
from random import randint
from datetime import datetime


class BankInfo:

    def __init__(self, bank_name: str, holder_name: str) -> None:
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_numbers = self.get_accounts_numbers()
        self.credit_histories = self.generate_credit_histories()
        self.transactions = self.generate_transactions_list()

    @staticmethod
    def get_credit_card_by_account_number(account_number):
        with open('credit_cards.json', encoding='utf-8') as f:
            credit_cards_data = json.load(f)
        found_card = None
        for card in credit_cards_data:
            if card["account_number"] == account_number:
                found_card = card
                break
        return found_card if found_card else None

    @staticmethod
    def get_accounts_numbers():
        with open('credit_cards.json', encoding='utf-8') as f:
            data = json.load(f)
        accounts_numbers = [item['account_number'] for item in data]
        return accounts_numbers

    @staticmethod
    def get_client_by_client_name(client_name):
        with open('credit_history.json', encoding='utf-8') as f:
            credit_histories_data = json.load(f)
        found_client = None
        for client in credit_histories_data:
            if client["holder_client_name"] == client_name:
                found_client = client
                break
        return found_client["credit_history"] if found_client else None

    def generate_credit_histories(self):
        credit_histories = []
        for account_number in self.accounts_numbers:
            credit_card: dict = self.get_credit_card_by_account_number(account_number)
            number_of_transactions: int = randint(2, 6)
            to_pay = 0
            account_credit_history = []

            for i in range(1, number_of_transactions):
                last_balance = credit_card["balance"]
                to_pay += randint(100, 500) * i // 2
                leftover = last_balance - to_pay
                credit_card["balance"] = leftover

                account_credit_history.append({
                    "payment_date": f"{randint(1, 30)}.{randint(1, 12)}.{datetime.now().year}",
                    "paid": to_pay,
                    "leftover": leftover})

            credit_histories.append({
                "holder_name": self.holder_name,
                "holder_client_name": credit_card["client_name"],
                "last_account_balance": leftover,
                "credit_history": account_credit_history
            })

        return credit_histories

    def generate_transactions_list(self):
        transactions_list = []
        for client in self.credit_histories:
            client_credit_history = client["credit_history"]
            client_transactions = []

            for payment in client_credit_history:
                client_transactions.append(f"{client['holder_client_name']} on {payment['payment_date']} "
                                           f"have successfully paid {payment['paid']}. "
                                           f"The leftover is: {payment['leftover']}")

            transactions_list.append({
                "client_name": client["holder_client_name"],
                "transactions": client_transactions
            })

        return transactions_list
