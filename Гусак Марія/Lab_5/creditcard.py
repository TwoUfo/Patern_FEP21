from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from cryptography.fernet import Fernet


@dataclass
class PersonalInfo:
    name: str
    number_of_accounts: int
    age: int
    passport_number: str

class CreditCard:
    def __init__(self, client: str, account_number: str, credit_limit: float, grace_period: int, cvv: str, encryption_key: bytes):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = self.encrypt(cvv, encryption_key)

    @property
    def cvv(self):
        return self.decrypt(self._cvv, self.encryption_key)

    @cvv.setter
    def cvv(self, value):
        self._cvv = self.encrypt(value, self.encryption_key)

    def encrypt(self, value, key):
        cipher_suite = Fernet(key)
        encrypted_value = cipher_suite.encrypt(value.encode())
        return encrypted_value

    def decrypt(self, encrypted_value, key):
        cipher_suite = Fernet(key)
        decrypted_value = cipher_suite.decrypt(encrypted_value).decode()
        return decrypted_value

    def give_details(self):
        return {
            "client": self.client,
            "account_number": self.account_number,
            "credit_limit": self.credit_limit,
            "grace_period": self.grace_period,
            "cvv": self.cvv
        }
