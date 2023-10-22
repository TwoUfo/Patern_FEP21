from abc import ABC, abstractmethod
from uuid import uuid4


class Item(ABC):

    def __init__(self, weight: float, count: int, ) -> None:
        self.id = uuid4()
        self.weight = weight
        self.count = count
        self.container_id = None

    @abstractmethod
    def get_total_weight(self):
        pass


class SmallItem(Item):
    def __init__(self, weight: float, count: int):
        super().__init__(weight, count)

    def get_total_weight(self):
        return self.weight * self.count


class HeavyItem(Item):
    def __init__(self, weight: float, count: int):
        super().__init__(weight, count)

    def get_total_weight(self):
        return self.weight * self.count


class RefrigeratedItem(Item):
    def __init__(self, weight: float, count: int):
        super().__init__(weight, count)

    def get_total_weight(self):
        return self.weight * self.count


class LiquidItem(Item):
    def __init__(self, weight: float, count: int):
        super().__init__(weight, count)

    def get_total_weight(self):
        return self.weight * self.count
