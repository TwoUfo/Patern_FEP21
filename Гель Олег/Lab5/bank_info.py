class BankInfo:
    def __init__(self, bank_name, holder_name, accounts_number):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = accounts_number
        self.credit_history = {}

    def give_details(self):
        return {
            "Банк": self.bank_name,
            "Власник рахунку": self.holder_name,
            "Номера рахунків": self.accounts_number,
        }

    def transaction_list(self, account_number):
        return ["Транзакція 1", "Транзакція 2"]
