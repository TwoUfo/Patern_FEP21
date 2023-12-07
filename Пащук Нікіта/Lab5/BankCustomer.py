from BankInfo import BankInfo
from CreditCard import CreditCard, ICreditCard
from dataclasses import dataclass
from typing import Optional
from abc import ABC, abstractmethod


class IBankCustomer(ABC):
    @abstractmethod
    def get_employment(self):
        pass

    @abstractmethod
    def give_details(self):
        pass


@dataclass
class PersonalInfo:
    credit_card: CreditCard
    contact_info: str
    birth_date: str
    employment: Optional[str]
    income_per_year: int


class BankCustomer(ICreditCard):
    def __init__(self, personal_info: PersonalInfo, bank_details: BankInfo):
        self._personal_info = personal_info
        self.bank_details = bank_details

    def get_employment(self):
        if self._personal_info.employment is not None:
            return self._personal_info.employment
        else:
            return "N/A"

    def give_details(self):
        credit_card_info = self._personal_info.credit_card.give_details()

        personal_info = {
            "Customer's contact info": self._personal_info.contact_info,
            "Customer's birth_date": self._personal_info.birth_date,
            "Customer's employment info": self.get_employment(),
            "Customer's income": self._personal_info.income_per_year,
            "Customer's credit card data": credit_card_info
        }

        account_number = self._personal_info.credit_card.account_number
        bank_info = {
            "Bank's name": self.bank_details.bank_name,
            "Account number": account_number,
            "Credit history": self.bank_details.transaction_list()
        }

        total_info = {
            "Customer's info": personal_info,
            "Bank's info": bank_info
        }

        return total_info
