from abc import ABC, abstractmethod
from uuid import uuid4


class Container(ABC):
    def __init__(self, weight: float) -> None:
        self.id = uuid4()
        self.weight = weight
        self._max_weight = 0
        self.items = []

    @abstractmethod
    def consumption(self) -> float:
        pass

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Container)
            and self.id == other.id
            and self.weight == other.weight
            and type(self) == type(other)
        )

    def get_max_weight(self) -> float:
        return self._max_weight


class BasicContainer(Container):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)
        self._max_weight = 4000

    def consumption(self) -> float:
        return self.weight * 2.5


class HeavyContainer(Container):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)
        self._max_weight = 5000

    def consumption(self) -> float:
        return self.weight * 3.0


class RefrigeratedContainer(HeavyContainer):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)
        self._max_weight = 7000

    def consumption(self) -> float:
        return self.weight * 5.0


class LiquidContainer(HeavyContainer):
    def __init__(self, weight: float) -> None:
        super().__init__(weight=weight)
        self._max_weight = 6000

    def consumption(self) -> float:
        return self.weight * 4.0
