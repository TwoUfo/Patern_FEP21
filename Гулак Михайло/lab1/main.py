from utils import (
    create_providers,
    create_customers,
    create_bills,
    select_provider_name,
    select_customer,
    print_bills,
)


if __name__ == "__main__":
    providers = create_providers()
    customers = create_customers(providers)

    for customer in customers:
        print(f"Set limits for every provider {customer.name} works with:")
        bills = create_bills(providers)

        customer.bills = bills

        companion = select_customer(customers, customer)
        provider_name = select_provider_name(providers)

        customer.talk(companion, provider_name, 1)
        customer.message(companion, provider_name, 1)
        customer.connect(provider_name, 10)

        print(f"{customer.name}'s bills: ")
        print_bills(bills)
