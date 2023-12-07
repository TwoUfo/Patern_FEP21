from abc import ABC, abstractmethod


class IItem(ABC):
    def __init__(self, id: str, weight: float, count: int, containerID: str, item_type: str):
        self.id = id
        self.weight = weight
        self.count = count
        self.containerID = containerID
        self.total_weight = 0
        self.item_type = item_type

    @abstractmethod
    def getTotalWeight(self):
        pass

    @staticmethod
    def check_type(id, weight, count, item_type=None, container_id=None):
        if weight <= 300 and item_type is None:
            return SmallItem(id, weight, count, container_id, "Small")
        elif weight > 300 and item_type is None:
            return HeavyItem(id, weight, count, container_id, "Heavy")
        elif item_type == "R":
            return RefrigeratedItem(id, weight, count, container_id, "Refrigerated")
        elif item_type == "L":
            return LiquidItem(id, weight, count, container_id, "Liquid")


class SmallItem(IItem):
    def __init__(self, id, weight, count, containerID, item_type):
        super().__init__(id, weight, count, containerID, item_type)

    def getTotalWeight(self):
        return self.weight * self.count


class HeavyItem(IItem):
    def __init__(self, id, weight, count, containerID, item_type):
        super().__init__(id, weight, count, containerID, item_type)

    def getTotalWeight(self):
        return self.weight * self.count


class RefrigeratedItem(IItem):
    def __init__(self, id, weight, count, containerID, item_type):
        super().__init__(id, weight, count, containerID, item_type)

    def getTotalWeight(self):
        return self.weight * self.count


class LiquidItem(IItem):
    def __init__(self, id, weight, count, containerID, item_type):
        super().__init__(id, weight, count, containerID, item_type)

    def getTotalWeight(self):
        return self.weight * self.count

