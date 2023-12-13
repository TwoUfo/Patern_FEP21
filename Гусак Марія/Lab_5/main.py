from flask import Flask, jsonify, request
from cryptography.fernet import Fernet
from bankcustomer import BankCustomer, PersonalInfo
from bankinfo import BankInfo
from creditcard import CreditCard

app = Flask(__name__)

encryption_key = Fernet.generate_key()
credit_card = CreditCard("John Doe", "1234-5678-9012-3456", 5000.0, 18, "123", encryption_key)
bank_info = BankInfo("MyBank", "Mary Husak", credit_card)
customer_info = PersonalInfo("John Doe", 1, 30, "AB123456")

customer = BankCustomer(customer_info, bank_info)

@app.route('/')
def home():
    return "Welcome to the Bank"

@app.route('/customer_details', methods=['GET'])
def get_customer_details():
    details = customer.give_details()
    return jsonify(details)

if __name__ == '__main__':
    app.run(debug=True)