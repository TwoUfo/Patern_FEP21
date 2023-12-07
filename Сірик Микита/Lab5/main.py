from classes.CreditCard import CreditCard
from classes.BankInfo import BankInfo

from faker import Faker
import json

fake = Faker(["uk_UA"])


def main():
    number_of_cards_to_generate = 5
    credit_cards = [CreditCard(
                fake.unique.name().split()[0],
                str(fake.unique.random_int(min=10_000_000_000, max=99_999_999_999)),
                fake.unique.random_int(min=150_000, max=250_000) + 50 * i,
                fake.unique.random_int(min=4, max=12),
                str(fake.unique.random_int(min=100, max=999))) for i in range(number_of_cards_to_generate)]

    with open('credit_cards.json', 'w', encoding='utf-8') as f:
        json.dump([card.get_details for card in credit_cards], f, indent=4, ensure_ascii=False)

    bank_info = BankInfo("PrivateBank", "Printoholic")

    with open('credit_history.json', 'w', encoding='utf-8') as file:
        json.dump(bank_info.credit_histories, file, indent=4, ensure_ascii=False)

    with open('transactions.json', 'w', encoding='utf-8') as file:
        json.dump(bank_info.transactions, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
