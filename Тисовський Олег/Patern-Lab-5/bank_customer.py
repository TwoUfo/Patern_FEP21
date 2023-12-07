from dataclasses import dataclass


@dataclass
class PersonalInfo:
    name: str
    age: int
    address: str


class BankCustomer:
    def __init__(self, personal_info, bank_info):
        self.personal_info = personal_info
        self.bank_info = bank_info

    def give_details(self, *args):
        bank_details = {
            "bank_name": self.bank_info.bank_name,
            "holder_name": self.bank_info.holder_name,
            "accounts_number": self.bank_info.accounts_number,
            "credit_history": self.bank_info.credit_history,
            "transaction_list": self.bank_info.transaction_list(self.bank_info.accounts_number[0])
        }

        personal_details = {
            "name": self.personal_info.name,
            "age": self.personal_info.age,
            "address": self.personal_info.address
        }

        details = {"personal_details": personal_details, "bank_details": bank_details}

        for arg in args:
            details[arg] = getattr(self, arg, None)

        return details


# Decorators for different types of customers
def IndividualCustomer(cls):
    class IndividualCustomerDecorator(cls):
        def give_details(self, *args):
            details = super().give_details(*args)
            details["Customer Type"] = "Individual Customer"
            return details
    return IndividualCustomerDecorator


def CorporateCustomer(cls):
    class CorporateCustomerDecorator(cls):
        def give_details(self, *args):
            details = super().give_details(*args)
            details["Customer Type"] = "Corporate Customer"
            return details
    return CorporateCustomerDecorator


def VIPCustomer(cls):
    class VIPCustomerDecorator(cls):
        def give_details(self, *args):
            details = super().give_details(*args)
            details["Customer Type"] = "VIP Customer"
            return details
    return VIPCustomerDecorator