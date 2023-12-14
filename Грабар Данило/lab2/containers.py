from abc import ABC, abstractmethod
from uuid import uuid4


class Container(ABC):
    def __init__(self, weight: float) -> None:
        self.id = uuid4()
        self.weight = weight

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
        return {
            "container id": self.id,
            "weight": self.weight
        }


class BasicContainer(Container):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def consumption(self) -> float:
        return self.weight * 2.5

    def serialize(self):
        data = super().serialize()
        data["consumption"] = self.consumption()
        return data


class HeavyContainer(Container):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def consumption(self) -> float:
        return self.weight * 3

    def serialize(self):
        data = super().serialize()
        data["consumption"] = self.consumption()
        return data


class RefrigeratedContainer(HeavyContainer):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def consumption(self) -> float:
        return self.weight * 5

    def serialize(self):
        data = super().serialize()
        data["consumption"] = self.consumption()
        return data


class LiquidContainer(HeavyContainer):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)

    def consumption(self) -> float:
        return self.weight * 4

    def serialize(self):
        data = super().serialize()
        data["consumption"] = self.consumption()
        return data
