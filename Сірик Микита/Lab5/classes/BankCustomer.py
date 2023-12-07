from dataclasses import dataclass
from classes.BankInfo import BankInfo


@dataclass
class PersonalInfo:
    name: str
    age: int
    id: int


class BankCustomer:

    def __int__(self, personal_info: PersonalInfo, bank_details: BankInfo) -> None:
        self.personal_info = personal_info
        self.bank_details = bank_details

    def give_details(self, *args) -> dict:
        pass
