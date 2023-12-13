from creditcard import CreditCard


class BankInfo:
    def __init__(self, bank_name: str, holder_name: str, card: CreditCard):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.card = card
        self.accounts_number = []

    def transaction_list(self):
        if self.bank_name and self.holder_name:
            self.accounts_number.append(self.card.account_number)
            return self.accounts_number
