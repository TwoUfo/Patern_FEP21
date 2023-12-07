from credit_card import CreditCard, GoldenCreditCard, CorporateCreditCard
from bank_info import BankInfo
from bank_customer import BankCustomer, IndividualCustomer, CorporateCustomer, VIPCustomer, PersonalInfo


def main():
    # Create instances with decorators
    golden_credit_card = GoldenCreditCard(CreditCard)("John Doe", "1234567890123456", 10000.0, 45, "123")
    corporate_credit_card = CorporateCreditCard(CreditCard)("Jane Doe", "9876543210987654", 20000.0, 60, "456")

    individual_customer = IndividualCustomer(BankCustomer)(PersonalInfo("Alice Smith", 28, "456 Main St"),
                                                           BankInfo("Example Bank", "Alice Smith", ["1111222233334444"],
                                                                    {"1111222233334444": ["2022-01-01: +$500",
                                                                                          "2022-02-01: -$200"]}))

    corporate_customer = CorporateCustomer(BankCustomer)(PersonalInfo("Bob Johnson", 35, "789 Business St"),
                                                         BankInfo("Example Bank", "Bob Johnson", ["5555666677778888"], {
                                                             "5555666677778888": ["2022-01-01: +$1000",
                                                                                  "2022-02-01: -$300"]}))

    vip_customer = VIPCustomer(BankCustomer)(PersonalInfo("Eve Williams", 40, "123 VIP Lane"),
                                             BankInfo("Example Bank", "Eve Williams", ["9999888877776666"], {
                                                 "9999888877776666": ["2022-01-01: +$2000", "2022-02-01: -$500"]}))

    # Test the decorated objects
    print("Golden Credit Card Details:")
    print(golden_credit_card.give_details())

    print("\nCorporate Credit Card Details:")
    print(corporate_credit_card.give_details())

    print("\nIndividual Customer Details:")
    print(individual_customer.give_details())

    print("\nCorporate Customer Details:")
    print(corporate_customer.give_details())

    print("\nVIP Customer Details:")
    print(vip_customer.give_details())


if __name__ == "__main__":
    main()
