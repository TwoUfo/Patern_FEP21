from customer import Customer
from operator import Operator


operator1 = Operator(0, "Kyivstar", 10, 6, 15, 20)
operator2 = Operator(1, "Vodafone", 9, 7, 10, 25)

customer1 = Customer(0, "Mary", 23, operator1, 100, 100)
customer2 = Customer(1, "David", 48, operator2, 150, 100)
operator1.generate_bill(100, 20, 500)
operator2.generate_bill(150, 70, 800)

print(f"Mary's bill is: {operator1.bill.sum}")
print(f"David's bill is: {operator2.bill.sum}")