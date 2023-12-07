from typing import List


class BankInfo:
    def __init__(self, bank_name: str, holder_name: str, accounts_number: List, credit_history: dict):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = accounts_number
        self.credit_history = credit_history

    def transaction_list(self):
        return self.credit_history
