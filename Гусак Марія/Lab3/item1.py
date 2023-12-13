from abc import ABC, abstractmethod
from uuid import uuid4

class Item:

    weight: float
    count: int
    containerID: int

    def weight(self, weight: float):
        self.weight = weight
        return self

    def count(self, count):
        self.count = count
        return self

    def containerID(self, containerID):
        self.containerID = containerID
        return self

    def build(self, item_type):

        if item_type == 'Small':
            return Small(self)
        elif item_type == 'Heavy':
            return Heavy(self)
        elif item_type == 'Refrigerated':
            return Refrigerated(self)
        elif item_type == 'Liquid':
            return Liquid(self)
        else:
            raise ValueError(f"Invalid item type: {item_type}")

class myItem(ABC):
    def __init__(self, item: Item):
        self.ID = int(uuid4())
        self.weight = item.weight
        self.count = item.count
        self.containerID = item.containerID

    @abstractmethod
    def get_total_weight(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Small(myItem):
    def __init__(self, item: Item):
        super().__init__(item)

    def __str__(self) -> str:
        return f"Small item with ID {self.ID} loaded."

    def get_total_weight(self):
        total_weight = self.weight * self.count
        print(f"Total weight of this item is {total_weight}")

class Heavy(myItem):
    def __init__(self, item: Item):
        super().__init__(item)

    def __str__(self) -> str:
        return f"Heavy item with ID {self.ID} loaded."

    def get_total_weight(self):
        total_weight = self.weight * self.count
        print(f"Total weight of this item is {total_weight}")


class Refrigerated(myItem):
    def __init__(self, item: Item):
        super().__init__(item)

    def __str__(self) -> str:
        return f"Refrigerated item with ID {self.ID} loaded."

    def get_total_weight(self):
        total_weight = self.weight * self.count
        print(f"Total weight of this item is {total_weight}")


class Liquid(myItem):
    def __init__(self, item: Item):
        super().__init__(item)

    def __str__(self) -> str:
        return f"Liquid item with ID {self.ID} loaded."

    def get_total_weight(self):
        total_weight = self.weight * self.count
        print(f"Total weight of this item is {total_weight}")

