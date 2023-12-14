from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import List

from app.schemas.items import Item


class Container(BaseModel, ABC):
    id: int

    @abstractmethod
    def consumption(self) -> float:
        pass

    @abstractmethod
    def add_item(self, item: Item):
        pass


class BasicContainer(Container):
    title: str
    weight: float
    items: List[Item] = []
    consumption: float

    def consumption(self) -> float:
        return self.weight * 2.5

    def add_item(self, item):
        self.items.append(item)


class HeavyContainer(Container):
    title: str
    weight: float
    items: List[Item] = []
    consumption: float

    def consumption(self) -> float:
        return self.weight * 3

    def add_item(self, item):
        self.items.append(item)


class RefrigeratedContainer(Container):
    title: str
    weight: float
    items: List[Item] = []
    consumption: float

    def consumption(self) -> float:
        return self.weight * 2.5

    def add_item(self, item):
        self.items.append(item)


class LiquidContainer(Container):
    title: str
    weight: float
    items: List[Item] = []
    consumption: float

    def consumption(self) -> float:
        return self.weight * 2.5

    def add_item(self, item):
        self.items.append(item)
