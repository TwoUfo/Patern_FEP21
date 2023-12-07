class Bill:
    """Клас для зберігання інформації про рахунок користувача."""

    def __init__(self, customer_id: int, limit: float) -> None:
        # Ініціалізуємо атрибути рахунку
        self.limit = limit  # Ліміт рахунку (максимальна сума боргу)
        self.customer_id = customer_id  # ID клієнта, якому належить рахунок
        self.current_debt = 0  # Поточний борг клієнта, на початку рівний 0

    def __str__(self) -> str:
        # Метод для отримання рядкового представлення рахунку
        return f"Current debt Bill = {self.current_debt}"

    def check_limit(self, value: float) -> bool:
        # Метод для перевірки, чи перевищено ліміт рахунку
        return value > self.limit

    def pay(self, value: float) -> None:
        # Метод для оплати частини боргу
        temp = self.current_debt - value
        if temp < 0:
            self.current_debt = 0  # Якщо борг оплачено повністю, обнуляємо поточний борг
        else:
            self.current_debt = temp
        print(f"Customer {self.customer_id} paid {value}")

    def add(self, debt: float) -> None:
        # Метод для додавання суми до поточного боргу
        temp = self.current_debt + debt
        if temp <= self.limit:
            self.current_debt = temp
            print(f"Added {debt} to debt")
        else:
            raise ValueError(f"You cannot exceed the limit of {self.limit}. Operation is forbidden")

    def change_limit(self, value: float) -> None:
        # Метод для зміни ліміту рахунку
        self.limit = value
        print(f"Limit has been increased to {self.limit}")
