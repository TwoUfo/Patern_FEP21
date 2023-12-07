from abc import ABC, abstractmethod
from uuid import uuid4

class Container(ABC):
    def __init__(self, weight: float) -> None:
        self.id = uuid4()
        self.weight = weight

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


class BasicContainer(Container):
    def __init__(self, weight: float):
        super().__init__(weight=weight)
    def consumption(self) -> float:
        return self.weight * 2.5

class HeavyContainer(Container):
    def __init__(self, weight: float):
        super().__init__(weight=weight)

    def consumption(self) -> float:
        return self.weight * 3.0

class RefrigeratedContainer(HeavyContainer):
    def __init__(self, weight: float):
        super().__init__(weight=weight)

    def consumption(self) -> float:
        return self.weight * 5.0

class LiquidContainer(HeavyContainer):
    def __init__(self, weight: float):
        super().__init__(weight=weight)

    def consumption(self) -> float:
        return self.weight * 4.0

class initContainer:
    @staticmethod
    def init_container(weight, value=None):
        if weight <= 3000:
            return BasicContainer(weight)

        elif value is None:
            return HeavyContainer(weight)

        elif value == 'R':
            return RefrigeratedContainer(weight)

        elif value == 'L':
            return LiquidContainer(weight)

