from abc import ABC, abstractmethod
from typing import Optional
from pydantic import BaseModel


class IItem(BaseModel, ABC):
    id: str
    weight: int
    count: int
    container_id: Optional[str]
    total_weight: int = 0
    item_type: str

    @abstractmethod
    def getTotalWeight(self):
        pass

    @staticmethod
    def check_type(id, weight, count, item_type, container_id=None):
        if item_type == "Small":
            return SmallItem(id=id, weight=weight, count=count, container_id=container_id, item_type=item_type)
        elif item_type == "Heavy":
            return HeavyItem(id=id, weight=weight, count=count, container_id=container_id, item_type=item_type)
        elif item_type == "Refrigerated":
            return RefrigeratedItem(id=id, weight=weight, count=count, container_id=container_id, item_type=item_type)
        elif item_type == "Liquid":
            return LiquidItem(id=id, weight=weight, count=count, container_id=container_id, item_type=item_type)


class SmallItem(IItem):
    def getTotalWeight(self):
        return self.weight * self.count


class HeavyItem(IItem):
    def getTotalWeight(self):
        return self.weight * self.count


class RefrigeratedItem(IItem):
    def getTotalWeight(self):
        return self.weight * self.count


class LiquidItem(IItem):
    def getTotalWeight(self):
        return self.weight * self.count

