
class Operator:
    def __init__(self, operator_id, name, talking_charge_per_minute, message_cost_per_message, discount_rate, network_cost_per_mb):
        # Ініціалізуємо атрибути оператора
        self.operator_id = operator_id
        self.name = name
        self.talking_charge_per_minute = talking_charge_per_minute
        self.message_cost_per_message = message_cost_per_message
        self.discount_rate = discount_rate
        self.network_cost_per_mb = network_cost_per_mb
class Customer:
    def __init__(self, customer_id, name, age, operator, balance, bill_limit):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.operator = operator
        self.balance = balance
        self.bill_limit = bill_limit
        self.bill = None

    # Метод для обчислення вартості розмови
    def calculate_talking_cost(self, minutes):
        talking_charge = minutes * self.operator.talking_charge_per_minute
        if self.age < 18 or self.age > 65:
            talking_charge *= (1 - self.operator.discount_rate)  # Застосовуємо знижку, якщо клієнт молодший 18 або старший 65 років
        return talking_charge

    # Метод для обчислення вартості повідомлень
    def calculate_message_cost(self, messages):
        message_cost = messages * self.operator.message_cost_per_message
        if self.operator == self.operator:
            message_cost *= (1 - self.operator.discount_rate)  # Застосовуємо знижку, якщо клієнти використовують одного оператора
        return message_cost

    # Метод для обчислення вартості інтернет-трафіку
    def calculate_internet_cost(self, mb_usage):
        return mb_usage * self.operator.network_cost_per_mb  # Обчислюємо вартість інтернет-трафіку

    # Метод для створення рахунку на основі дій клієнта
    def generate_bill(self, minutes, messages, mb_usage):
        total_cost = self.calculate_talking_cost(minutes) + self.calculate_message_cost(messages) + self.calculate_internet_cost(mb_usage)

        if self.bill_limit is None or total_cost <= self.bill_limit:
            self.bill = Bill(self.customer_id, total_cost)  # Створюємо об'єкт рахунку, якщо вартість не перевищує ліміт
        else:
            print("Bill limit exceeded. No bill generated.")  # Виводимо повідомлення, якщо вартість перевищила ліміт

# Клас, що представляє рахунок клієнта
class Bill:
    def __init__(self, customer_id, amount):
        self.customer_id = customer_id
        self.amount = amount


operator1 = Operator(0, "Operator1", 0.2, 0.05, 0.1, 0.01)
operator2 = Operator(1, "Operator2", 0.3, 0.06, 0.2, 0.02)

Andre = Customer(0, "Andre", 20, operator1, 100, 200)
Alex = Customer(1, "Alex", 48, operator1, 150, 300)
Dennis = Customer(2, "Dennis", 70, operator2, 200, 250)

Andre.generate_bill(100, 20, 500)
Alex.generate_bill(150, 70, 800)
Dennis.generate_bill(20, 100, 1000)

# Виводимо суму рахунків для кожного клієнта
print(f"Andre bill amount: ${Andre.bill.amount}")
print(f"Alex bill amount: ${Alex.bill.amount}")
print(f"Dennis bill amount: ${Dennis.bill.amount}")
