import hashlib


class CreditCard:
    def __init__(self, client, account_number, credit_limit, grace_period, cvv):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv_hash = self._hash_cvv(cvv)

    def _hash_cvv(self, cvv):
        return hashlib.sha256(cvv.encode()).hexdigest()

    @property
    def cvv(self):
        return self._decrypt(self._cvv_hash)

    @cvv.setter
    def cvv(self, value):
        self._cvv_hash = self._hash_cvv(value)

    def give_details(self, *args):
        details = {
            "Client": self.client,
            "Account Number": self.account_number,
            "Credit Limit": self.credit_limit,
            "Grace Period": self.grace_period,
            "CVV": self.cvv
        }
        return details

    def _encrypt(self, value):
        cipher = Cipher(algorithms.AES(self._cvv_hash), modes.CFB(b'\0' * 16), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_value = encryptor.update(value.encode()) + encryptor.finalize()
        return urlsafe_b64encode(encrypted_value)

    def _decrypt(self, value):
        cipher = Cipher(algorithms.AES(self._cvv_hash), modes.CFB(b'\0' * 16), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_value = decryptor.update(urlsafe_b64decode(value)) + decryptor.finalize()
        return decrypted_value.decode()


def GoldenCreditCard(cls):
    class GoldenCreditCardDecorator(cls):
        def give_details(self, *args):
            details = super().give_details(*args)
            details["Card Type"] = "Golden Credit Card"
            return details
    return GoldenCreditCardDecorator


def CorporateCreditCard(cls):
    class CorporateCreditCardDecorator(cls):
        def give_details(self, *args):
            details = super().give_details(*args)
            details["Card Type"] = "Corporate Credit Card"
            return details
    return CorporateCreditCardDecorator

