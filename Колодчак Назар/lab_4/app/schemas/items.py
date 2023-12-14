from abc import ABC, abstractmethod
from pydantic import BaseModel

class Item(BaseModel, ABC):

    id: int
    title: str
    weight: int
    count: int
    container_id: int

    @abstractmethod
    def get_total_weight(self) -> int:
        pass

class SmallItem(Item):

    def get_total_weight(self) -> int:
        return self.weight * self.count

class HeavyItem(Item):

    def get_total_weight(self) -> int:
        return self.weight * self.count

class RefrigeratedItem(Item):

    def get_total_weight(self) -> int:
        return self.weight * self.count

class LiquidItem(Item):

    def get_total_weight(self) -> int:
        return self.weight * self.count
