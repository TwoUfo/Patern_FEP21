from abc import ABC, abstractmethod
from typing import Optional
from app.schemas.items import BasicItem, HeavyItem, RefrigeratedItem, LiquidItem
from pydantic import BaseModel


class Container(BaseModel):
    id: int
    weight: float
    port_id: int
    ship_id: Optional[int] = None


    def consumption(self) -> float:
        pass


    def can_load_item(self, item) -> bool:
        pass

    def load_items(self, items):
        for item in items:
            if self.can_load_item(item):
                self.items.append(item)

    def unload_items(self):
        unloaded_items = self.items[:]
        self.items = []
        return unloaded_items

    def __eq__(self, other) -> bool:
        id_check = self.id == other.id
        weight_check = self.weight == other.weight
        type_check = self.__class__ == other.__class__
        if id_check and weight_check and type_check:
            return True
        else:
            return False

    class Config:
        orm_mode = True
        from_attributes = True


class BasicContainer(Container):

    def __repr__(self):
        return f"Basic cont with ID {self.id}"

    def can_load_item(self, item):
        return isinstance(item, BasicItem)

    def consumption(self) -> float:
        return self.weight * 2.5


class HeavyContainer(Container):

    def __repr__(self):
        return f"Heavy cont with ID {self.id}"

    def consumption(self) -> float:
        return self.weight * 3.0


class RefrigeratedContainer(Container):

    def __repr__(self):
        return f"Refrigerated cont with ID {self.id}"

    def can_load_item(self, item):
        return isinstance(item, HeavyItem)

    def can_load_item(self, item):
        return isinstance(item, RefrigeratedItem)

    def consumption(self) -> float:
        return self.weight * 5.0


class LiquidContainer(Container):

    def __repr__(self):
        return f"Liquid cont with ID {self.id}"

    def can_load_item(self, item):
        return isinstance(item, LiquidItem)

    def consumption(self) -> float:
        return self.weight * 4.0

