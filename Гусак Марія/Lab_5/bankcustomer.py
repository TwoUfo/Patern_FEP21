from bankinfo import BankInfo
from creditcard import *


class BankCustomer:
    def __init__(self, personal_info: PersonalInfo, bank_details: BankInfo):
        self.personal_info = personal_info
        self.bank_details = bank_details

    def give_details(self):
        details = {
            "personal_info": self.personal_info.__dict__,
            "bank_details": self.bank_details.__dict__,
            "transaction_history": self.bank_details.transaction_list()
        }
        return details
