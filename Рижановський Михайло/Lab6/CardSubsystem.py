import sqlite3


class Payment:
    db_connection = sqlite3.connect("lab6.db")
    db_cursor = db_connection.cursor()

    def __init__(self, card_number, balance, cvv, date, total_price):
        self.card_number = card_number
        self.balance = balance
        self.cvv = cvv
        self.date = date
        self.total_price = total_price

    @classmethod
    def add_credit_card(cls, card_number, balance, cvv, date):
        # Add input validation if needed (e.g., check card number format)
        cls.db_cursor.execute('''
            SELECT COUNT(*) FROM credit_card WHERE card_number = ?
        ''', (card_number,))
        count = cls.db_cursor.fetchone()[0]

        if count == 0:
            cls.db_cursor.execute('''
                INSERT INTO credit_card (card_number, balance, cvv, date_expired) VALUES (?, ?, ?, ?)
            ''', (card_number, balance, cvv, date))
            cls.db_connection.commit()
            return True
        else:
            print(f"Credit card with number '{card_number}' already exists in the database.")
            return False

    def update_balance(self, balance, total_price):
        new_balance = balance - total_price
        self.db_cursor.execute('''
            UPDATE credit_card
            SET balance = ?
            WHERE card_number = ?
        ''', (new_balance, self.card_number))
        self.db_connection.commit()
        return f"New credit card balance: {new_balance}"

    def verify(self):
        if self.total_price > self.balance:
            return False
        return True

# Add a credit card
# Payment.add_credit_card('1234567890123456', 1000, '123', '12/24')
#
# # Create a credit card instance
# credit_card_instance = Payment('1234567890123456', 1000, '123', '12/24', 500)
#
# # Verify the payment
# if credit_card_instance.verify():
#     print("Payment verified. Processing payment...")
#     # Update the balance
#     updated_balance_message = Payment.update_balance('1234567890123456', credit_card_instance.total_price, credit_card_instance.balance)
#     print(updated_balance_message)
# else:
#     print("Insufficient funds. Payment cannot be processed.")
