from customer import Customer
from operators import Operator
from bill import Bill
from typing import Dict


operators_data: Dict[str, Operator] = {
#словник для операторів
    "Operator1": Operator(1, 'jong', 23.0, 2.0, 2.0, 10),
    "Operator2": Operator(2, 'myckailo', 21.0, 1.0, 1.0, 2),
}

bills_data: Dict[str, Bill] = {
#словник для рахунків
    "Operator1": Bill(1, 3000.0),
    "Operator2": Bill(2, 30010.0),
}

customers = [
#лист для клієнтів
    Customer(operators_data, bills_data, 1, "John", "Doe", 30),
    Customer(operators_data, bills_data, 1, "Jane", "Smith", 25),
]

def print_menu():
#Вибір операцій
    print("Choose an option:")
    print("1. Customer talks using Operator1")
    print("2. Customer talks using Operator2")
    print("3. Customer sends messages using Operator1")
    print("4. Customer sends messages using Operator2")
    print("5. Customer connects to the network using Operator1")
    print("6. Customer connects to the network using Operator2")
    print("7. Pay off debt for Operator1")
    print("8. Pay off debt for Operator2")
    print("9. Pay a bill for Operator1")
    print("10. Pay a bill for Operator2")
    print("11. Change limit for Operator1")
    print("12. Change limit for Operator2")
    print("13. View bills")
    print("0. Exit")

while True:
#цикл для вибору операцій
    print_menu()
    choice = input("Enter your choice: ")

    if choice == "0":
        break
    elif choice == "1":
        customers[0].talk(23, customers[0], customers[1], "Operator1")
    elif choice == "2":
        customers[0].talk(31, customers[0], customers[1], "Operator2")
    elif choice == "3":
        customers[0].message(25, customers[0], customers[1], "Operator1")
    elif choice == "4":
        customers[0].message(11, customers[0], customers[1], "Operator2")
    elif choice == "5":
        customers[0].connect(25, "Operator1")
    elif choice == "6":
        customers[0].connect(28, "Operator2")
    elif choice == "7":
        customers[0].pay_off_debt('Operator1')
    elif choice == "8":
        customers[0].pay_off_debt('Operator2')
    elif choice == "9":
        operator_name = "Operator1"
        amount = customers[0].bills[operator_name].current_debt
        customers[0].pay_bill(operator_name, amount)
    elif choice == "10":
        operator_name = "Operator2"
        amount = customers[0].bills[operator_name].current_debt
        customers[0].pay_bill(operator_name, amount)
    elif choice == "11":
        operator_name = "Operator1"
        amount = float(input("Enter the amount to change limit for Operator1: "))
        customers[0].change_limit(amount, operator_name)
    elif choice == "12":
        operator_name = "Operator2"
        amount = float(input("Enter the amount to change limit for Operator2: "))
        customers[0].change_limit(amount, operator_name)
    elif choice == "13":
        customers[0].view_bills()
    else:
        print("Invalid choice. Please try again.")
