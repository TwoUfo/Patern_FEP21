from abc import ABC, abstractmethod
from uuid import UUID, uuid4
from dataclasses import dataclass, field

from .items import Item, RefrigeratedItem, LiquidItem


@dataclass(repr=True, eq=True)
class Container(ABC):
    id: UUID = field(init=False, default=uuid4())
    max_weight: int = 0
    current_weight: int = field(init=False, default=0)
    items: list = field(init=False, default_factory=list)

    @abstractmethod
    def consumption(self) -> float:
        pass

    def load(self, item: Item):
        if item in self.items:
            print(f"Item with id {item.id} is already loaded.")
            return

        item_weight = item.get_total_weight()

        if self.current_weight + item_weight > self.max_weight:
            print("Unable to load item into container: no place left.")
            return

        item.container_id = self.id
        self.current_weight += item_weight
        self.items.append(item)

    def unload(self) -> list:
        unloaded_items = [*self.items]

        self.items.clear()

        return unloaded_items


@dataclass(repr=True, eq=True)
class BasicContainer(Container):
    def consumption(self) -> float:
        return self.current_weight * 2.5

    def load(self, item: Item) -> bool:
        if item in self.items:
            print(f"Item with id {item.id} is already loaded.")
            return False

        item_weight = item.get_total_weight()

        if self.current_weight + item_weight > self.max_weight:
            print("Unable to load item into container: no place left.")
            return False

        if isinstance(item, (RefrigeratedItem, LiquidItem)):
            print("Unable to load refrigerated or liquid item in basic container.")
            return False

        item.container_id = self.id
        self.current_weight += item_weight
        self.items.append(item)
        return True


@dataclass(repr=True, eq=True)
class HeavyContainer(Container):
    def consumption(self) -> float:
        return self.current_weight * 3.0


@dataclass(repr=True, eq=True)
class RefrigeratedContainer(HeavyContainer):
    def consumption(self) -> float:
        return self.current_weight * 5.0


@dataclass(repr=True, eq=True)
class LiquidContainer(HeavyContainer):
    def consumption(self) -> float:
        return self.current_weight * 4.0
