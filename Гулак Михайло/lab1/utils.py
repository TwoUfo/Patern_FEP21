from classes import Provider, Customer, Bill


def create_customers(providers: dict) -> list:
    customers = []

    while True:
        try:
            name, age, discount_rate = input(
                "Enter customer's name , age and discount rate separated by space: "
            ).split(" ")
            age = int(age)
            discount_rate = float(discount_rate)

            if discount_rate < 0 or discount_rate > 1:
                raise ValueError()

            customer = Customer(name, age, discount_rate, providers)
            customers.append(customer)

        except ValueError:
            print(
                "Age must be an integer and discount rate should be a floating number (greater than zero and less than one)."
            )

        except KeyboardInterrupt:
            break

    # To prevent appearing text on the same line after CTRL + C was pressed
    print()

    return customers


def create_providers() -> tuple[dict]:
    providers = {}

    while True:
        try:
            name = input("Enter provider's name: ")
            talking_charge, message_cost, network_charge = [
                float(charge)
                for charge in input(
                    "Enter talking charge , message cost and network charge separated by space: "
                ).split(" ")
            ]

            if talking_charge < 0 or message_cost < 0 or network_charge < 0:
                raise ValueError()

            providers[name] = Provider(
                name, talking_charge, message_cost, network_charge
            )

        except ValueError:
            print(
                "All the costs and charges must be a floating number equals to or greater than zero."
            )

        except KeyboardInterrupt:
            break

    # To prevent appearing text on the same line after CTRL + C was pressed
    print()

    return providers


def create_bills(providers: dict) -> dict:
    bills = {}

    for provider_name in providers.keys():
        try:
            limit = float(input("Enter bill limit: "))
            if limit <= 0:
                raise ValueError()

            bill = Bill(limit)
            bills[provider_name] = bill

        except ValueError:
            print("Limit should be a floating number greater than zero.")

        except KeyboardInterrupt:
            break

    # To prevent appearing text on the same line after CTRL + C was pressed
    print()

    return bills


def print_provider_names(providers: dict):
    for index, provider_name in enumerate(providers.keys(), start=1):
        print(f"{index}. {provider_name}")


def print_bills(bills: dict):
    for provider, bill in bills.items():
        print(f"Bill for {provider}: {bill}")


def print_customers(customers: list, customer_to_exclude: Customer = None):
    if customer_to_exclude:
        customers = [_ for _ in customers if _.id != customer_to_exclude.id]

    for customer_id, customer in enumerate(customers, start=1):
        print(f"{customer_id}. {customer.name}")


def select_provider_name(providers: dict) -> str:
    print("Select provider to use: ")
    print_provider_names(providers)

    while True:
        try:
            index = int(input("Enter name index: "))

            if index <= 0:
                raise ValueError()

            return list(providers.keys())[index - 1]

        except ValueError:
            print("Index must be an integer greater than zero.")


def select_customer(customers: list, customer_to_exclude: Customer):
    print("Select companion to interact with: ")
    print_customers(customers, customer_to_exclude)

    while True:
        try:
            index = int(input("Enter customer index: "))

            if index <= 0:
                raise ValueError()

            return customers[index - 1]

        except ValueError:
            print("Index must be an integer greater than zero.")
