class Customer:
    def __init__(self, ID, name, age, operators, bills, limitingAmount):
        self.ID = ID
        self.name = name
        self.age = age
        self.operators = operators
        self.bills = bills
        self.limitingAmount = limitingAmount
        self.current_operator = None

    def receive_call(self, minute):
        print(f"{self.name} received a call for {minute} minutes.")

    def talk(self, minute, other_customer):
        if self.current_operator:
            talking_cost = self.current_operator.calculate_talking_cost(minute, self)
            if self.bills[self.current_operator.ID].check(talking_cost):
                self.bills[self.current_operator.ID].add(talking_cost)
                other_customer.receive_call(minute)
                print(f"{self.name} made a call to {other_customer.name} for {minute} minutes.")
                self.display_balance(self.current_operator.ID)  # Отображаем баланс
            else:
                print(f"{self.name} cannot make a call due to insufficient balance.")
        else:
            print(f"{self.name} does not have an operator. Please assign one.")

    def message(self, quantity, other_customer):
        if self.current_operator:
            message_cost = self.current_operator.calculate_message_cost(quantity, self, other_customer)
            if self.bills[self.current_operator.ID].check(message_cost):
                self.bills[self.current_operator.ID].add(message_cost)
                other_customer.receive_message(quantity)
                print(f"{self.name} sent {quantity} messages to {other_customer.name}.")
                self.display_balance(self.current_operator.ID)  # Отображаем баланс
            else:
                print(f"{self.name} cannot send messages due to insufficient balance.")
        else:
            print(f"{self.name} does not have an operator. Please assign one.")

    def connection(self, amount):
        if self.current_operator:
            network_cost = self.current_operator.calculate_network_cost(amount)
            if self.bills[self.current_operator.ID].check(network_cost):
                self.bills[self.current_operator.ID].add(network_cost)
                print(f"{self.name} connected to the internet for {amount} MB.")
                self.display_balance(self.current_operator.ID)  # Отображаем баланс
            else:
                print(f"{self.name} cannot connect to the internet due to insufficient balance.")
        else:
            print(f"{self.name} does not have an operator. Please assign one.")

    def pay_bill(self, operator_id, amount):
        if operator_id < len(self.bills) and self.bills[operator_id].check(amount):
            self.bills[operator_id].pay(amount)
            print(f"{self.name} paid {amount} to Operator {operator_id}.")
            self.display_balance(operator_id)

    def change_operator(self, new_operator):
        self.current_operator = new_operator
        print(f"{self.name} changed the operator to Operator {new_operator.ID}.")

    def change_bill_limit(self, new_limit):
        for bill in self.bills:
            bill.change_limit(new_limit)
        print(f"{self.name} changed the bill limit to {new_limit}.")

    def display_balance(self, operator_id):
        balance = self.bills[operator_id].currentDebt
        print(f"{self.name}'s current balance with Operator {operator_id}: {balance}")


class Operator:
    def __init__(self, ID, talkingCharge, messageCost, networkCharge, discountRate):
        self.ID = ID
        self.talkingCharge = talkingCharge
        self.messageCost = messageCost
        self.networkCharge = networkCharge
        self.discountRate = discountRate

    def calculate_talking_cost(self, minute, customer):
        if customer.age < 18 or customer.age > 65:
            return minute * (self.talkingCharge * (1 - self.discountRate / 100))
        else:
            return minute * self.talkingCharge

    def calculate_message_cost(self, quantity, customer, other_customer):
        if customer.current_operator == other_customer.current_operator:
            return quantity * (self.messageCost * (1 - self.discountRate / 100))
        else:
            return quantity * self.messageCost

    def calculate_network_cost(self, amount):
        return amount * self.networkCharge


class Bill:
    def __init__(self, limitingAmount):
        self.limitingAmount = limitingAmount
        self.currentDebt = 0

    def check(self, amount):
        return self.currentDebt + amount <= self.limitingAmount

    def add(self, amount):
        self.currentDebt += amount

    def pay(self, amount):
        if self.currentDebt >= amount:
            self.currentDebt -= amount
        else:
            self.currentDebt = 0

    def change_limit(self, new_limit):
        self.limitingAmount = new_limit


class Main:
    def __init__(self):
        self.customers = []
        self.operators = []
        self.bills = []
        self.input_data = []  # Store all input data

    def load_data(self):
        while True:
            try:
                num_customers = int(input("Enter the number of customers (or 'stop' to display all data): "))
                if num_customers < 0:
                    print("Invalid input. Please enter a positive number.")
                    continue
                elif num_customers == 0:
                    self.display_all_data()
                    break
            except ValueError:
                print("Invalid input. Please enter a number or 'stop'.")

            customer_data = []  # Store customer data

            for i in range(num_customers):
                ID = int(input(f"Enter ID for customer {i + 1}: "))
                name = input(f"Enter name for customer {i + 1}: ")
                age = int(input(f"Enter age for customer {i + 1}: "))

                operators = []
                num_operators = int(input(f"Enter the number of operators for customer {i + 1}: "))
                operator_data = []  # Store operator data

                for j in range(num_operators):
                    operator_ID = int(input(f"Enter operator ID for customer {i + 1}, operator {j + 1}: "))
                    talking_charge = float(input(f"Enter talking charge for operator {j + 1}: "))
                    message_cost = float(input(f"Enter message cost for operator {j + 1}: "))
                    network_charge = float(input(f"Enter network charge for operator {j + 1}: "))
                    while True:
                        discount_rate_input = input(f"Enter discount rate for operator {j + 1}: ")
                        if discount_rate_input.strip() != "":
                            discount_rate = float(discount_rate_input)
                            break
                        else:
                            print("Discount rate cannot be empty. Please enter a valid value.")
                    operator_data.append((operator_ID, talking_charge, message_cost, network_charge, discount_rate))
                    operator = Operator(operator_ID, talking_charge, message_cost, network_charge, discount_rate)
                    operators.append(operator)

                bill_limit = float(input(f"Enter bill limit for customer {i + 1}: "))
                bill = Bill(bill_limit)
                bill_data = (bill_limit,)

                customer_data.append((ID, name, age, operator_data, bill_data))
                customer = Customer(ID, name, age, operators, [bill], bill_limit)
                self.customers.append(customer)
                self.operators.extend(operators)
                self.bills.append(bill)

            self.input_data.append((num_customers, customer_data))

    def process_actions(self):
        # Implement the logic to process the actions based on the input data
        pass

    def run(self):
        self.load_data()
        self.process_actions()

    def display_all_data(self):
        print("All input data:")
        for num_customers, customer_data in self.input_data:
            print(f"Number of customers: {num_customers}")
            for customer_info in customer_data:
                ID, name, age, operator_data, bill_data = customer_info
                print(f"Customer ID: {ID}, Name: {name}, Age: {age}")
                for operator_info in operator_data:
                    operator_ID, talking_charge, message_cost, network_charge, discount_rate = operator_info
                    print(f"Operator ID: {operator_ID}, Talking Charge: {talking_charge}, Message Cost: {message_cost}, Network Charge: {network_charge}, Discount Rate: {discount_rate}")
                bill_limit = bill_data[0]
                print(f"Bill Limit: {bill_limit}")
            print()


# Sample usage
if __name__ == "__main__":
    main = Main()
    main.run()
