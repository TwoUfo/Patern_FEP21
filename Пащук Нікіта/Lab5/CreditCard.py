from cryptography.fernet import Fernet
from abc import ABC, abstractmethod


class ICreditCard(ABC):
    @abstractmethod
    def give_details(self):
        pass


class CreditCard(ICreditCard):
    def __init__(self, client: str, account_number: str, credit_limit: int, grace_period: int, cvv: str):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = cvv
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    @property
    def cvv(self):
        decrypted_value = self.cipher.decrypt(self._cvv)
        return decrypted_value.decode()

    @cvv.setter
    def cvv(self, value):
        self._cvv = self.encrypt(value)

    def give_details(self):
        details = {
            "Client": self.client,
            "Account number": self.account_number,
            "Credit limit": self.credit_limit,
            "Grace period": self.grace_period,
            "Cvv": self._cvv
        }
        return details

    def encrypt(self, value):
        encrypted_value = self.cipher.encrypt(value.encode())
        return encrypted_value

    def decrypt(self):
        decrypted_value = self.cipher.decrypt(self._cvv)
        return decrypted_value.decode()


def golden_credit_card_decorator(cls):
    class GoldenCreditCardDecorator(cls):
        def __init__(self, client, account_number, credit_limit, grace_period, cvv):
            super().__init__(client, account_number, credit_limit, grace_period, cvv)
            self.grace_period += 20

    return GoldenCreditCardDecorator


def normal_credit_card_decorator(cls):
    class NormalCreditCardDecorator(cls):
        def __init__(self, client, account_number, credit_limit, grace_period, cvv):
            super().__init__(client, account_number, credit_limit, grace_period, cvv)
            self.grace_period += 5

    return NormalCreditCardDecorator


@normal_credit_card_decorator
class NormalCreditCard(CreditCard):
    pass


@golden_credit_card_decorator
class GoldenCreditCard(CreditCard):
    pass


def create_credit_card(client: str, account_number: str, credit_limit: int, grace_period: int, cvv: str):
    if credit_limit < 7000:
        return NormalCreditCard(client, account_number, credit_limit, grace_period, cvv)
    else:
        return GoldenCreditCard(client, account_number, credit_limit, grace_period, cvv)
