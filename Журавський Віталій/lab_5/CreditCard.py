from cryptography.fernet import Fernet


class CreditCard:
    def __init__(self, client, account_number, credit_limit, grace_period, cvv):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._key = Fernet.generate_key()
        self._cvv = self.encrypt(cvv)

    def encrypt(self, data):
        cipher = Fernet(self._key)
        encrypted_data = cipher.encrypt(data.encode())
        return encrypted_data

    def decrypt(self):
        cipher = Fernet(self._key)
        decrypted_data = cipher.decrypt(self._cvv).decode()
        return decrypted_data

    def give_details(self):
        return {
            'client': self.client,
            'account_number': self.account_number,
            'credit_limit': self.credit_limit,
            'grace_period': self.grace_period,
            'cvv': self._cvv,
        }



