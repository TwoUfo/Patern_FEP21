class Operator:
    def __init__(self, operator_id):
        self.operator_id = operator_id
        print(f"Створено оператора {self.operator_id}")

class Customer:
    def __init__(self, customer_id, balance, operator_id, bill_limit):
        self.customer_id = customer_id
        self.balance = balance
        self.operator_id = operator_id
        self.bill_limit = bill_limit
        print(f"Створено клієнта {self.customer_id}")

    def talk_to_customer(self, other_customer, message):
        print(f"Клієнт {self.customer_id} розмовляє з клієнтом {other_customer.customer_id}: {message}")

    def send_message(self, other_customer, message):
        print(f"Клієнт {self.customer_id} відправляє повідомлення клієнту {other_customer.customer_id}: {message}")

    def connect_to_internet(self):
        print(f"Клієнта {self.customer_id} під'єднано до інтернету")

    def pay_bills(self, amount):
        if amount > self.balance:
            print("Помилка: Сума платежу перевищує баланс клієнта.")
        else:
            self.balance -= amount
            print(f"Клієнт {self.customer_id} сплатив рахунок. Новий баланс: {self.balance}")

    def change_operator(self, new_operator):
        self.operator_id = new_operator.operator_id
        print(f"Клієнт {self.customer_id} змінив оператора на Оператор {new_operator.operator_id}")

    def change_bill_limit(self, new_limit):
        self.bill_limit = new_limit
        print(f"Клієнт {self.customer_id} змінив ліміт рахунку на {new_limit}")

operator1 = Operator(operator_id=1)

customer1 = Customer(customer_id=1, balance=100, operator_id=1, bill_limit=50)
customer2 = Customer(customer_id=2, balance=50, operator_id=1, bill_limit=40)

customer1.talk_to_customer(customer2, "Привіт, як у вас справи?")
customer2.send_message(customer1, "Привіт! У мене все добре, дякую.")

customer1.connect_to_internet()

customer1.pay_bills(60)
customer1.change_operator(operator1)
customer1.change_bill_limit(75)
