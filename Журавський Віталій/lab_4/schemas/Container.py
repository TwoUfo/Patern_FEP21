from abc import ABC, abstractmethod
from uuid import uuid4


class Container(ABC):
    def __init__(self, weight: float, ID) -> None:
        self.id = ID
        self.weight = weight
        self.curr_items = []

    @abstractmethod
    def consumption(self) -> float:
        pass

    def __eq__(self, other):
        id_check = self.id == other.id
        weight_check = self.weight == other.weight
        check_type = self.__class__ == other.__class__

        if id_check and weight_check and check_type:
            return True
        else:
            return False

    def load_item(self, items):
        self.weight += items.weight*items.count
        self.curr_items.append(items)

    @staticmethod
    def init_container(weight, value=None, ID=None):
        if weight <= 3000:
            return BasicContainer(weight, ID)

        elif value is None:
            return HeavyContainer(weight, ID)

        elif value == 'R':
            return RefrigeratedContainer(weight, ID)

        elif value == 'L':
            return LiquidContainer(weight, ID)


class BasicContainer(Container):
    def __init__(self, weight: float, ID):
        super().__init__(weight=weight, ID=ID)
        self.type = 'Basic'

    def consumption(self) -> float:
        return self.weight * 2.5


class HeavyContainer(Container):
    def __init__(self, weight: float, ID):
        super().__init__(weight=weight, ID=ID)
        self.type = 'Heavy'

    def consumption(self) -> float:
        return self.weight * 3.0


class RefrigeratedContainer(HeavyContainer):
    def __init__(self, weight: float, ID):
        super().__init__(weight=weight, ID=ID)
        self.type = 'Refrigerated'

    def consumption(self) -> float:
        return self.weight * 5.0


class LiquidContainer(HeavyContainer):
    def __init__(self, weight: float, ID):
        super().__init__(weight=weight, ID=ID)
        self.type = 'Liquid'

    def consumption(self) -> float:
        return self.weight * 4.0

