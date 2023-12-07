from random import randint


class CreditCard:

    def __init__(self, client_name: str, account_number: str, credit_limit: float, grace_period: int, cvv: str) -> None:
        self.client_name = client_name
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self.dollar_balance = 100_000
        self.hashed_cvv = cvv

    @property
    def get_details(self) -> dict:
        """Return details about the client's credit card."""
        return {
            "client_name": self.client_name,
            "account_number": self.account_number,
            "credit_limit": self.credit_limit,
            "grace_period": self.grace_period,
            "balance": self.dollar_balance + (self.dollar_balance * randint(5, 100) * 5 // 100),
            "hashed_cvv": self.encrypt_cvv()
        }

    def encrypt_cvv(self) -> int:
        """Encrypts the given value."""
        return hash(self.hashed_cvv)

    def decrypt_cvv(self, cvv) -> bool:
        """Decrypts the given value."""
        return self.hashed_cvv == hash(cvv)
