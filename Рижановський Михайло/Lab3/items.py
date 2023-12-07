from dataclasses import dataclass
from abc import ABC, abstractmethod
from uuid import uuid4

@dataclass
class Item:
    id: str
    weight: float
    count: int
    containerID: int
    specificAttribute: str

    def get_total_weight(self):
        total_weight = self.weight * self.count
        return total_weight

    def serialize_item(self):
        return {
            "type": self.__class__.__name__,
            "id": str(self.id),
            "weight": self.weight,
            "count": self.count,
            "containerID": self.containerID,
            "specificAttribute": self.specificAttribute,
            "total weight": self.get_total_weight()
        }

class ItemFactory:
    @staticmethod
    def create_item(item_type: str, weight, count, containerID, specificAttribute):
        new_id = str(uuid4())
        if item_type == "Small item":
            return SmallItems(new_id, weight, count, containerID, specificAttribute)
        elif item_type == "Heavy item":
            return HeavyItems(new_id, weight, count, containerID, specificAttribute)
        elif item_type == "Refrigerated item":
            return RefrigeratedItem(new_id, weight, count, containerID, specificAttribute)
        elif item_type == "Liquid item": 
            return LiquidItems(new_id, weight, count, containerID, specificAttribute)
        else:
            raise ValueError(f"Invalid item type: {item_type}")


    
class SmallItems(Item):
    def __init__(self, ID, weight, count, containerID, specificAttribute):
        super().__init__(ID, weight, count, containerID,specificAttribute)

    def get_total_weight(self):
        return self.weight * self.count    

    def serialize(self):
        return self.serialize_item()


class HeavyItems(SmallItems):
    def __init__(self, ID, weight, count, containerID, specificAttribute):
        super().__init__(ID, weight, count, containerID,specificAttribute)

    def get_total_weight(self):
        return self.weight * self.count

    def serialize(self):
        return self.serialize_item()
    

class RefrigeratedItem(HeavyItems):
    def __init__(self, ID, weight, count, containerID, specificAttribute):
        super().__init__(ID, weight, count, containerID,specificAttribute)

    def get_total_weight(self):
        return self.weight * self.count
    
    def serialize(self):
        return self.serialize_item()

class LiquidItems(RefrigeratedItem):
    def __init__(self, ID, weight, count, containerID, specificAttribute):
        super().__init__(ID, weight, count, containerID,specificAttribute)

    def get_total_weight(self):
        return self.weight * self.count
    
    def serialize(self):
        return self.serialize_item()
