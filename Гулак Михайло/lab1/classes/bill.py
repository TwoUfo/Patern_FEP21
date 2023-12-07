from uuid import uuid4


class Bill:
    def __init__(self, limit=100, debt=0):
        self.id = uuid4()
        self.limit = limit
        self.debt = debt

    def is_limit_reached(self, cost: float) -> bool:
        if self.debt + cost >= self.limit:
            return True

        return False

    def increase_debt(self, value: float) -> None:
        self.debt += value

    def pay_debt(self, value: float) -> None:
        if self.debt < 0:
            self.limit -= value
            self.debt = 0
        else:
            self.debt -= value

    def change_limit(self, value: float) -> None:
        if value < 0:
            raise Exception("No value provided.")

        self.limit = value

    def __repr__(self):
        return f"Bill(id={self.id},limit={self.limit}, debt={self.debt})"
