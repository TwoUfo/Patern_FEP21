from uuid import UUID, uuid4
from abc import ABC
from dataclasses import dataclass, field


import helpers


@dataclass(repr=True, eq=True)
class Item(ABC):
    id: UUID = field(init=False, default=uuid4())
    container_id: UUID = None
    weight: float = 0
    count: int = 0

    def get_total_weight(self) -> float:
        return self.weight * self.count

    @staticmethod
    def create(type, **kwargs):
        if not type:
            raise ValueError("No type provided.")

        item_cls = helpers.ITEMS_MAPPING.get(type)

        return item_cls(**kwargs)


@dataclass(repr=True, eq=True)
class SmallItem(Item):
    def __init__(self, container_id: UUID = None, weight: float = 0, count: int = 1):
        super().__init__(container_id, weight, count)


@dataclass(repr=True, eq=True)
class HeavyItem(Item):
    def __init__(self, container_id: UUID = None, weight: float = 0, count: int = 1):
        super().__init__(container_id, weight, count)


@dataclass(repr=True, eq=True)
class RefrigeratedItem(Item):
    def __init__(self, container_id: UUID = None, weight: float = 0, count: int = 1):
        super().__init__(container_id, weight, count)


@dataclass(repr=True, eq=True)
class LiquidItem(Item):
    def __init__(self, container_id: UUID = None, weight: float = 0, count: int = 1):
        super().__init__(container_id, weight, count)
