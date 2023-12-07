from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING
from pydantic import BaseModel

from app.schemas.items import Item


class Container(BaseModel, ABC):

    id: int
    title: str
    weight: int
    _max_weight = int
    items: List[Item] = []

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

    def get_max_weight(self) -> int:
        return self._max_weight


class BasicContainer(Container):

    _max_weight = 4000

    def consumption(self) -> float:
        return self.weight * 2.5


class HeavyContainer(Container):

    _max_weight = 5000

    def consumption(self) -> float:
        return self.weight * 3.0


class RefrigeratedContainer(HeavyContainer):

    _max_weight = 7000

    def consumption(self) -> float:
        return self.weight * 5.0


class LiquidContainer(HeavyContainer):

    _max_weight = 6000

    def consumption(self) -> float:
        return self.weight * 4.0
