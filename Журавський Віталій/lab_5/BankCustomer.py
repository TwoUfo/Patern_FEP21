from dataclasses import dataclass


@dataclass
class PersonalInfo:
    name: str
    age: int
    curr_position: str


class BankCustomer:
    def __init__(self, personal_info, credit_card, bank_info):
        self.personal_info = personal_info
        self.credit_card = credit_card
        self.bank_info = bank_info

    def give_details(self):
        credit_card_details = self.credit_card.give_details()
        t_list = self.bank_info.transaction_list(self.credit_card.account_number)

        bank_info_details = {
            'bank_name': self.bank_info.bank_name,
            'holder_name': self.bank_info.holder_name,
            'transaction_list': t_list
        }

        personal_info = {
            'name': self.personal_info.name,
            'age': self.personal_info.age,
            'current_position': self.personal_info.curr_position
        }

        return {
            'personal_info': personal_info,
            'credit_card_details': credit_card_details,
            'bank_info_details': bank_info_details
        }


class VipDecorator:
    def __init__(self, customer):
        self._customer = customer

    def give_details(self):
        details = self._customer.give_details()
        details['personal_info']['Vip'] = True
        return details


class VipBankCustomer(BankCustomer):
    def __init__(self, customer):
        super().__init__(customer.personal_info, customer.credit_card, customer.bank_info)
        self._decorator = VipDecorator(customer)

    def give_details(self):
        return self._decorator.give_details()


class CorporateDecorator:
    def __init__(self, customer):
        self._customer = customer

    def give_details(self):
        details = self._customer.give_details()
        details['personal_info']['Corporate'] = True
        return details


class CorporateBankCustomer(BankCustomer):
    def __init__(self, customer):
        super().__init__(customer.personal_info, customer.credit_card, customer.bank_info)
        self._decorator = CorporateDecorator(customer)

    def give_details(self):
        return self._decorator.give_details()

