class BankInfo:
    def __init__(self, bank_name, holder_name):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = ["5678901234567890", "1234567890123456",
                                "9876543210987654", "3456789012345678", "7890123456789012"]

        self.credit_history = {}

    def add_account(self, credit_card):
        if credit_card.account_number not in self.accounts_number:
            self.accounts_number.append(credit_card.account_number)
            self.credit_history[credit_card.account_number] = []

    def add_transaction(self, account_number, transaction):
        if account_number in self.accounts_number:
            self.credit_history[account_number].append(transaction)

    def transaction_list(self, account_number):
        if account_number in self.accounts_number:
            return self.credit_history[account_number]

