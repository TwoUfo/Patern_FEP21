from dataclasses import dataclass

@dataclass
class PersonalInfo:
    pass

class BankCustomer:
    def __init__(self, personal_info, bank_details):
        self.personal_info = personal_info
        self.bank_details = bank_details

    def give_details(self):
        details = self.bank_details.give_details()
        details["Список транзакцій"] = self.bank_details.transaction_list(
            self.bank_details.accounts_number[0]
        )
        return details

    def access_vip_lounge(self):
        print("Доступ до VIP-зони наданий")

