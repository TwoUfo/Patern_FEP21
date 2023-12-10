import hashlib

class CreditCard:
    def __init__(self, client, account_number, credit_limit, grace_period, cvv):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = self.encrypt(cvv)  # Захищено хешуванням

    @property
    def cvv(self):
        return self.decrypt(self._cvv)

    @cvv.setter
    def cvv(self, value):
        self._cvv = self.encrypt(value)

    def give_details(self):
        return {
            "Клієнт": self.client,
            "Номер рахунку": self.account_number,
            "Кредитний ліміт": self.credit_limit,
            "Грейс-період": self.grace_period,
            "CVV": self.cvv
        }

    def encrypt(self, value):
        hashed_value = hashlib.sha256(value.encode()).hexdigest()
        return hashed_value

    def decrypt(self, value):
        return "Розшифрування не підтримується"


def golden_credit_card_decorator(cls):
    class GoldenCreditCardDecorator(cls):
        def apply_golden_discount(self):
            print("Застосовано знижку для золотої кредитної картки")

        def additional_functionality(self):
            print("Додатковий функціонал для золотої кредитної картки")

        def access_vip_lounge(self):
            print("Додатковий функціонал для VIP-клієнтів")

    return GoldenCreditCardDecorator
