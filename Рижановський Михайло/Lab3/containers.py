from abc import ABC, abstractmethod
from uuid import uuid4
from items import *

class Container(ABC):
    def __init__(self, weight: float) -> None:
        self.id = uuid4()
        self.weight = weight
        self.items = []  

    @abstractmethod
    def consumption(self) -> float:
        pass

    def __eq__(self, other) -> bool:
        id_check = self.id == other.id
        weight_check = self.weight == other.weight
        type_check = self.__class__ == other.__class__
        if id_check and weight_check and type_check:
            return True
        else:
            return False

    def serialize(self):
        data = {
            "type": self.__class__.__name__,
            "id": str(self.id),
            "weight": self.weight,
            "consumption": self.consumption(),
            "items": [item.serialize() for item in self.items]
        }
        return data
    
    def add_item(self, item):
        if self.remaining_capacity() >= item.weight:
            self.items.append(SmallItems)
            return True
        else:
            return False

class BasicContainer(Container):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def consumption(self) -> float:
        return self.weight * 2.5
    
    def add_item(self, item):
        self.items.append(item)

class HeavyContainer(Container):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def consumption(self) -> float:
        return self.weight * 3
    
    def add_item(self, item):
        self.items.append(item)

class RefrigeratedContainer(Container):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def consumption(self) -> float:
        return self.weight * 5
    
    def add_item(self, item):
        self.items.append(item)

class LiquidContainer(Container):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def consumption(self) -> float:
        return self.weight * 4

    def add_item(self, item):
        self.items.append(item)
