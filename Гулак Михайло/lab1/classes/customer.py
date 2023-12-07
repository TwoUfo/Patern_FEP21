from uuid import uuid4


class Customer:
    def __init__(
        self, name, age, discount_rate=0, providers: dict = None, bills: dict = None
    ):
        self.id = uuid4()
        self.name = name
        self.age = age
        self.discount_rate = discount_rate
        self.providers = providers
        self.bill = bills

    def talk(self, customer, provider_name: str, duration: int) -> None:
        if len(provider_name) == 0:
            raise Exception("No provider name given.")

        if duration <= 0:
            raise Exception("Duration should be greater than zero.")

        provider = self.providers[provider_name]
        bill = self.bills[provider_name]

        cost = provider.calculate_talking_cost(self, duration)
        if bill.is_limit_reached(cost):
            print(f"{self.name} had reached limit.")
        else:
            bill.increase_debt(cost)
            print(f"{self.name} talks with {customer.name} for {duration} minute(s)")

    def message(self, customer, provider_name: str, quantity: int) -> None:
        if len(provider_name) == 0:
            raise Exception("No provider name given.")

        if quantity <= 0:
            raise Exception("Quantity should be greater than zero.")

        provider = self.providers[provider_name]
        bill = self.bills[provider_name]

        cost = provider.calculate_message_cost(self, quantity)
        if bill.is_limit_reached(cost):
            print(f"{self.name} reaches limit.")
        else:
            bill.increase_debt(cost)
            print(f"{self.name} sends to {customer.name} {quantity} message(s)")

    def connect(self, provider_name: str, data_size: int) -> None:
        if len(provider_name) == 0:
            raise Exception("No provider name given.")

        if data_size <= 0:
            raise Exception("Data size should be greater than zero.")

        provider = self.providers[provider_name]
        bill = self.bills[provider_name]

        cost = provider.calculate_network_charge(self, data_size)
        if bill.is_limit_reached(cost):
            print(f"{self.name} reaches limit.")
        else:
            bill.increase_debt(cost)
            print(
                f"{self.name} upload / download {data_size} MB through internet connection."
            )

    def __repr__(self):
        return f"Customer(id={self.id}, name={self.name}, age={self.age}, discount_rate={self.discount_rate})"
