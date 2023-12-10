from credit_card import CreditCard, golden_credit_card_decorator
from bank_info import BankInfo
from bank_customer import BankCustomer, PersonalInfo

def main():

    CreditCardWithDiscount = golden_credit_card_decorator(CreditCard)
    credit_card = CreditCardWithDiscount("Андрій Бувалий", "UA2231820988881345123441952301", 5000, 30, "310")

    bank_info = BankInfo("Банк Львів", "Андрій Бувалий", ["UA2231820988881345123441952301"])
    bank_customer = BankCustomer(PersonalInfo(), bank_info)

    print("=== Адаптер ===")
    print("Інформація про кредитну картку:")
    print(credit_card.give_details())

    print("\nІнформація про клієнта банку (з адаптером):")
    print(bank_customer.give_details())

    print("\n=== Декоратор ===")
    credit_card.apply_golden_discount()
    credit_card.additional_functionality()
    credit_card.access_vip_lounge()

    vip_customer = BankCustomer(PersonalInfo(), bank_info)
    vip_customer.access_vip_lounge()

if __name__ == "__main__":
    main()
