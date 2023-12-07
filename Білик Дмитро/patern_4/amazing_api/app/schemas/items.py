from abc import ABC, abstractmethod
from uuid import UUID

from pydantic import BaseModel


class Item(BaseModel, ABC):
    id: int
    weight: float
    type : str
    port_id: int


    @abstractmethod
    def get_total_weight(self) -> float:
        pass


class ItemFactory(ABC):
    @abstractmethod
    def create_item(self, weight: float, containerID: UUID) -> Item:
        pass


class BasicItem(Item):
    def get_total_weight(self) -> float:
        return self.weight * 1.5


class HeavyItem(Item):
    def get_total_weight(self) -> float:
        return self.weight * 3.0


class RefrigeratedItem(Item):
    def get_total_weight(self) -> float:
        return self.weight * 4.0


class LiquidItem(Item):
    def get_total_weight(self) -> float:
        return self.weight * 5.0


class ItemFactory(ABC):
    @abstractmethod
    def create_item(self, weight: float, count: int, containerID: UUID) -> Item:
        pass


class BasicItemFactory(ItemFactory):
    def create_item(self, weight: float,containerID: UUID) -> BasicItem:
        return BasicItem(id=0, weight=weight, containerID=containerID)


class HeavyItemFactory(ItemFactory):
    def create_item(self, weight: float,containerID: UUID) -> HeavyItem:
        return HeavyItem(id=0, weight=weight,containerID=containerID)


class RefrigeratedItemFactory(ItemFactory):
    def create_item(self, weight: float, containerID: UUID) -> RefrigeratedItem:
        return RefrigeratedItem(id=0, weight=weight,  containerID=containerID)


class LiquidItemFactory(ItemFactory):
    def create_item(self, weight: float, containerID: UUID) -> LiquidItem:
        return LiquidItem(id=0, weight=weight, containerID=containerID)
